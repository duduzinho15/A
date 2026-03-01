import React, { useState, useEffect } from 'react';
import { getHealth, triggerHeal, getAgentLogs } from '../services/api';
import { Activity, ShieldAlert, Cpu, HardDrive, Database, RefreshCw, Terminal, AlertTriangle, CheckCircle2 } from 'lucide-react';

interface HealthData {
    status: string;
    components: {
        database: string;
        disk: { percent: number; free_gb: number; status?: string };
        memory: { percent: number };
    };
}

const DebugHeal: React.FC = () => {
    const [health, setHealth] = useState<HealthData | null>(null);
    const [logs, setLogs] = useState<string[]>([]);
    const [isHealing, setIsHealing] = useState(false);
    const [message, setMessage] = useState<{ type: 'success' | 'error' | 'info', text: string } | null>(null);

    const fetchData = async () => {
        try {
            const [healthRes, logsRes] = await Promise.all([
                getHealth(),
                getAgentLogs()
            ]);
            setHealth(healthRes.data);
            setLogs(logsRes.data.logs || []);
        } catch (error) {
            console.error('Error fetching debug data:', error);
        }
    };

    useEffect(() => {
        fetchData();
        const interval = setInterval(fetchData, 5000);
        return () => clearInterval(interval);
    }, []);

    const handleHeal = async () => {
        if (!window.confirm('Executar procedimento de Auto-Healing de Emergência? Isso tentará corrigir conexões de banco e limpar arquivos temporários.')) return;

        setIsHealing(true);
        setMessage({ type: 'info', text: 'Iniciando diagnóstico e reparo...' });

        try {
            const res = await triggerHeal();
            if (res.data.status === 'success' || res.data.repaired) {
                setMessage({ type: 'success', text: 'Procedimento de reparo concluído com sucesso!' });
            } else {
                setMessage({ type: 'info', text: 'Scanning concluído. Nenhum problema crítico detectado.' });
            }
            fetchData();
        } catch (error) {
            setMessage({ type: 'error', text: 'Falha ao executar procedimento de healing.' });
        } finally {
            setIsHealing(false);
            setTimeout(() => setMessage(null), 5000);
        }
    };

    return (
        <div className="flex flex-col gap-8 animate-in fade-in duration-500">
            {/* Header Cards */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                <div className="glass p-6 rounded-2xl border-white/5 bg-gradient-to-br from-white/5 to-transparent">
                    <div className="flex items-center gap-3 mb-4">
                        <div className={`p-2 rounded-lg ${health?.status === 'healthy' ? 'bg-neonGreen/10 text-neonGreen' : 'bg-neonRed/10 text-neonRed'}`}>
                            <Activity size={20} />
                        </div>
                        <span className="text-sm font-bold opacity-60 uppercase tracking-widest">Global Status</span>
                    </div>
                    <div className="text-2xl font-black tracking-tighter uppercase italic">
                        {health?.status || 'PENDING...'}
                    </div>
                </div>

                <div className="glass p-6 rounded-2xl border-white/5">
                    <div className="flex items-center gap-3 mb-4">
                        <div className="p-2 rounded-lg bg-neonBlue/10 text-neonBlue">
                            <Cpu size={20} />
                        </div>
                        <span className="text-sm font-bold opacity-60 uppercase tracking-widest">Memory</span>
                    </div>
                    <div className="flex items-end gap-2">
                        <span className="text-3xl font-black tracking-tighter">{health?.components.memory.percent.toFixed(0)}%</span>
                        <div className="flex-1 h-2 bg-white/5 rounded-full mb-2 overflow-hidden">
                            <div
                                className="h-full bg-neonBlue transition-all duration-1000"
                                style={{ width: `${health?.components.memory.percent}%` }}
                            />
                        </div>
                    </div>
                </div>

                <div className="glass p-6 rounded-2xl border-white/5">
                    <div className="flex items-center gap-3 mb-4">
                        <div className="p-2 rounded-lg bg-neonCyan/10 text-neonCyan">
                            <HardDrive size={20} />
                        </div>
                        <span className="text-sm font-bold opacity-60 uppercase tracking-widest">Storage</span>
                    </div>
                    <div className="text-2xl font-black tracking-tighter">
                        {health?.components.disk.free_gb} GB FREE
                    </div>
                </div>

                <div className="glass p-6 rounded-2xl border-white/5">
                    <div className="flex items-center gap-3 mb-4">
                        <div className={`p-2 rounded-lg ${health?.components.database === 'connected' ? 'bg-neonGreen/10 text-neonGreen' : 'bg-neonRed/10 text-neonRed'}`}>
                            <Database size={20} />
                        </div>
                        <span className="text-sm font-bold opacity-60 uppercase tracking-widest">Database</span>
                    </div>
                    <div className="text-xl font-bold">
                        {health?.components.database === 'connected' ? 'CONNECTED' : 'DISCONNECTED'}
                    </div>
                </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                {/* Terminal Area */}
                <div className="lg:col-span-2 flex flex-col gap-4">
                    <div className="glass rounded-2xl border-white/5 overflow-hidden flex flex-col h-[500px]">
                        <div className="px-6 py-4 border-b border-white/5 flex justify-between items-center bg-white/5">
                            <div className="flex items-center gap-2">
                                <Terminal size={18} className="text-neonCyan" />
                                <span className="text-xs font-bold uppercase tracking-widest opacity-80">Deep Diagnostics Log</span>
                            </div>
                            <div className="flex gap-2">
                                <div className="w-2 h-2 rounded-full bg-neonRed/50" />
                                <div className="w-2 h-2 rounded-full bg-neonYellow/50" />
                                <div className="w-2 h-2 rounded-full bg-neonGreen/50" />
                            </div>
                        </div>
                        <div className="flex-1 p-6 font-mono text-xs overflow-y-auto space-y-1 bg-black/40">
                            {logs.length > 0 ? logs.map((log, i) => (
                                <div key={i} className="flex gap-3 opacity-80 hover:opacity-100 transition-opacity">
                                    <span className="text-white/20 select-none">{(i + 1).toString().padStart(3, '0')}</span>
                                    <span className={`${log.includes('ERRO') || log.includes('CRITICAL') ? 'text-neonRed shadow-[0_0_5px_rgba(255,20,147,0.3)]' : log.includes('WARNING') ? 'text-neonYellow' : 'text-white/70'}`}>
                                        {log}
                                    </span>
                                </div>
                            )) : (
                                <div className="h-full flex items-center justify-center opacity-20 italic">
                                    Waiting for system telemetry...
                                </div>
                            )}
                        </div>
                    </div>
                </div>

                {/* Action Panel */}
                <div className="flex flex-col gap-6">
                    <div className="glass p-8 rounded-3xl border-neonRed/10 relative overflow-hidden group">
                        <div className="absolute top-0 right-0 p-4 opacity-5 group-hover:opacity-10 transition-opacity">
                            <ShieldAlert size={120} />
                        </div>
                        <h3 className="text-xl font-bold mb-2 flex items-center gap-2 text-neonRed">
                            <AlertTriangle size={24} /> MAINTENANCE
                        </h3>
                        <p className="text-xs text-white/40 mb-8 leading-relaxed">
                            O módulo de Auto-Healing detecta e corrige automaticamente falhas de infraestrutura,
                            vazamento de memória e inconsistências de estado.
                        </p>

                        <button
                            onClick={handleHeal}
                            disabled={isHealing}
                            className={`w-full py-4 rounded-2xl font-black tracking-widest uppercase transition-all flex items-center justify-center gap-3 overflow-hidden relative shadow-lg ${isHealing
                                ? 'bg-white/5 text-white/20 cursor-not-allowed'
                                : 'bg-neonRed text-white hover:shadow-[0_0_30px_rgba(255,20,147,0.4)] active:scale-95'
                                }`}
                        >
                            {isHealing ? (
                                <>
                                    <RefreshCw size={20} className="animate-spin" />
                                    HEALING_SYSTEM...
                                </>
                            ) : (
                                <>
                                    <ShieldAlert size={20} />
                                    RUN EMERGENCY HEAL
                                </>
                            )}
                            {isHealing && (
                                <div className="absolute bottom-0 left-0 h-1 bg-white/20 animate-loading-bar" style={{ width: '100%' }} />
                            )}
                        </button>

                        {message && (
                            <div className={`mt-6 p-4 rounded-xl text-xs font-bold border animate-in zoom-in duration-300 ${message.type === 'success' ? 'bg-neonGreen/10 border-neonGreen/20 text-neonGreen' :
                                message.type === 'error' ? 'bg-neonRed/10 border-neonRed/20 text-neonRed' :
                                    'bg-neonBlue/10 border-neonBlue/20 text-neonBlue'
                                } flex items-center gap-2`}>
                                {message.type === 'success' ? <CheckCircle2 size={16} /> : <Activity size={16} />}
                                {message.text}
                            </div>
                        )}
                    </div>

                    <div className="glass p-8 rounded-3xl border-white/5 flex-1">
                        <h4 className="text-sm font-bold opacity-60 uppercase tracking-widest mb-6">Repair Checklist</h4>
                        <ul className="space-y-4">
                            {[
                                { label: 'DB Connection Watchdog', active: health?.components.database === 'connected' },
                                { label: 'Temporary Files Cleanup', active: true },
                                { label: 'Ghost Jobs Termination', active: true },
                                { label: 'SSL Certificate Monitor', active: true },
                                { label: 'Ollama Memory Flush', active: true }
                            ].map((item, idx) => (
                                <li key={idx} className="flex items-center gap-3 text-[10px] font-bold tracking-widest uppercase">
                                    <div className={`w-1.5 h-1.5 rounded-full ${item.active ? 'bg-neonGreen shadow-[0_0_5px_#39ff14]' : 'bg-white/10'}`} />
                                    <span className={item.active ? 'text-white/80' : 'text-white/20'}>{item.label}</span>
                                </li>
                            ))}
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default DebugHeal;
