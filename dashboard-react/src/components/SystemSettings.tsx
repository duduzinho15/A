import React, { useState, useEffect } from 'react';
import { getConfig, updateConfig } from '../services/api';
import { Settings, Save, RefreshCw, AlertCircle, CheckCircle2, Sliders, Lock } from 'lucide-react';

const SystemSettings: React.FC = () => {
    const [config, setConfig] = useState<Record<string, string>>({});
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [message, setMessage] = useState<{ type: 'success' | 'error', text: string } | null>(null);

    const fetchConfig = async () => {
        try {
            const res = await getConfig();
            setConfig(res.data);
        } catch (error) {
            console.error('Error fetching config:', error);
            setMessage({ type: 'error', text: 'Falha ao carregar configurações.' });
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchConfig();
    }, []);

    const handleChange = (key: string, value: string) => {
        setConfig(prev => ({ ...prev, [key]: value }));
    };

    const handleSave = async () => {
        setSaving(true);
        setMessage(null);
        try {
            const res = await updateConfig(config);
            if (res.data.status === 'success') {
                setMessage({ type: 'success', text: 'Configurações salvas com sucesso! O sistema aplicará as mudanças em breve.' });
            } else {
                setMessage({ type: 'error', text: res.data.message || 'Erro ao salvar.' });
            }
        } catch (error) {
            setMessage({ type: 'error', text: 'Falha na comunicação com o servidor.' });
        } finally {
            setSaving(false);
            setTimeout(() => setMessage(null), 5000);
        }
    };

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-[400px]">
                <RefreshCw className="animate-spin text-neonCyan" size={40} />
            </div>
        );
    }

    return (
        <div className="max-w-4xl mx-auto flex flex-col gap-8 animate-in slide-in-from-bottom duration-500">
            <div className="flex justify-between items-center">
                <div>
                    <h2 className="text-2xl font-black tracking-tighter uppercase italic flex items-center gap-3">
                        <Sliders className="text-neonCyan" /> System Configuration
                    </h2>
                    <p className="text-white/40 text-xs mt-1 uppercase tracking-widest">Ajuste os parâmetros de operação da fábrica</p>
                </div>

                <button
                    onClick={handleSave}
                    disabled={saving}
                    className={`px-8 py-3 rounded-2xl font-black tracking-widest uppercase transition-all flex items-center gap-3 shadow-lg ${saving
                            ? 'bg-white/5 text-white/20 cursor-not-allowed'
                            : 'bg-neonCyan text-background hover:shadow-[0_0_30px_rgba(0,243,255,0.4)] active:scale-95'
                        }`}
                >
                    {saving ? <RefreshCw className="animate-spin" size={18} /> : <Save size={18} />}
                    {saving ? 'SAVING...' : 'SAVE_CHANGES'}
                </button>
            </div>

            {message && (
                <div className={`p-4 rounded-2xl text-xs font-bold border flex items-center gap-3 animate-in fade-in duration-300 ${message.type === 'success' ? 'bg-neonGreen/10 border-neonGreen/20 text-neonGreen' : 'bg-neonRed/10 border-neonRed/20 text-neonRed'
                    }`}>
                    {message.type === 'success' ? <CheckCircle2 size={18} /> : <AlertCircle size={18} />}
                    {message.text}
                </div>
            )}

            <div className="grid grid-cols-1 gap-6">
                {/* Environment Variables Card */}
                <div className="glass p-8 rounded-3xl border-white/5 bg-gradient-to-br from-white/5 to-transparent">
                    <div className="flex items-center gap-3 mb-8">
                        <Settings className="text-white/40" size={20} />
                        <h3 className="text-sm font-bold uppercase tracking-widest opacity-80">Pipeline & Agent Variables</h3>
                    </div>

                    <div className="space-y-8">
                        {Object.keys(config).length > 0 ? Object.entries(config).map(([key, value]) => (
                            <div key={key} className="flex flex-col md:flex-row md:items-center justify-between gap-4 group">
                                <div className="flex-1">
                                    <label className="text-[10px] font-black tracking-widest text-white/40 uppercase mb-2 block group-hover:text-neonCyan transition-colors">
                                        {key.replace(/_/g, ' ')}
                                    </label>
                                    <div className="relative">
                                        <input
                                            type="text"
                                            value={value}
                                            onChange={(e) => handleChange(key, e.target.value)}
                                            className="w-full bg-black/40 border border-white/10 rounded-xl px-4 py-3 text-sm focus:border-neonCyan focus:ring-1 focus:ring-neonCyan/20 outline-none transition-all font-mono"
                                        />
                                    </div>
                                </div>
                                <div className="hidden md:block w-32 text-right">
                                    <span className="text-[8px] opacity-20 font-mono italic">.env key: {key}</span>
                                </div>
                            </div>
                        )) : (
                            <div className="text-center py-12 opacity-20">
                                <Lock size={48} className="mx-auto mb-4" />
                                <p className="text-xs uppercase tracking-widest">Nenhuma variável permitida encontrada.</p>
                            </div>
                        )}
                    </div>
                </div>

                {/* Info Card */}
                <div className="glass p-8 rounded-3xl border-neonCyan/10 flex items-start gap-6 bg-neonCyan/5">
                    <div className="w-12 h-12 rounded-2xl bg-neonCyan/10 flex items-center justify-center text-neonCyan shrink-0 shadow-[0_0_15px_rgba(0,243,255,0.1)]">
                        <AlertCircle size={24} />
                    </div>
                    <div>
                        <h4 className="font-bold text-sm mb-2">Segurança & Persistência</h4>
                        <p className="text-xs text-white/50 leading-relaxed">
                            As alterações feitas aqui são persistidas diretamente no arquivo <code className="text-neonCyan bg-white/5 px-1 rounded">.env</code> do servidor.
                            Alguns serviços podem precisar de um ciclo de reinicialização para ler os novos valores.
                            O **Agent Sentinel** monitora essas mudanças para ajustar seu comportamento de orquestração dinamicamente.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default SystemSettings;
