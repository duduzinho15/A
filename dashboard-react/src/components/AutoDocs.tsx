import React, { useState, useEffect } from 'react';
import { FileText, RefreshCw, CheckCircle, AlertTriangle, ShieldCheck } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import { getChangelog, runAutoDocs } from '../services/api';

const AutoDocs: React.FC = () => {
    const [changelog, setChangelog] = useState<string>('');
    const [loading, setLoading] = useState<boolean>(true);
    const [updating, setUpdating] = useState<boolean>(false);
    const [status, setStatus] = useState<{ type: 'success' | 'error' | 'none', message: string }>({ type: 'none', message: '' });

    const fetchChangelog = async () => {
        try {
            const response = await getChangelog();
            setChangelog(response.data.content || '# Changelog Vazio');
        } catch (error) {
            console.error('Erro ao buscar changelog:', error);
            setChangelog('# Erro ao carregar changelog');
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchChangelog();
    }, []);

    const handleUpdateDocs = async () => {
        setUpdating(true);
        setStatus({ type: 'none', message: '' });
        try {
            const response = await runAutoDocs();
            if (response.data.success) {
                setStatus({ type: 'success', message: 'Documentação atualizada com sucesso!' });
                await fetchChangelog();
            } else {
                setStatus({ type: 'error', message: response.data.error || 'Falha ao atualizar.' });
            }
        } catch (error) {
            setStatus({ type: 'error', message: 'Erro de conexão com o agente.' });
            console.error('Update failed:', error);
        } finally {
            setUpdating(false);
        }
    };

    return (
        <div className="space-y-6 animate-fade-in">
            {/* Header / Actions */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 glass-card p-6">
                <div className="flex items-center gap-3">
                    <div className="p-3 bg-neon-green/10 rounded-xl">
                        <ShieldCheck className="w-6 h-6 text-neon-green" />
                    </div>
                    <div>
                        <h2 className="text-xl font-bold text-white tracking-tight">Auto-Docs & Audit</h2>
                        <p className="text-sm text-gray-400">Auditoria automática de código e registro de changelog via IA.</p>
                    </div>
                </div>

                <button
                    onClick={handleUpdateDocs}
                    disabled={updating}
                    className={`flex items-center justify-center gap-2 px-6 py-3 rounded-xl font-bold transition-all duration-300 ${updating
                            ? 'bg-gray-700 cursor-not-allowed opacity-50'
                            : 'bg-neon-green text-black hover:shadow-[0_0_20px_rgba(57,255,20,0.4)] hover:scale-105 active:scale-95'
                        }`}
                >
                    <RefreshCw className={`w-5 h-5 ${updating ? 'animate-spin' : ''}`} />
                    {updating ? 'Escaneando Código...' : 'Scan & Update Docs'}
                </button>
            </div>

            {/* Status Alert */}
            {status.type !== 'none' && (
                <div className={`flex items-center gap-3 p-4 rounded-xl border ${status.type === 'success'
                        ? 'bg-green-500/10 border-green-500/50 text-green-400'
                        : 'bg-red-500/10 border-red-500/50 text-red-400'
                    }`}>
                    {status.type === 'success' ? <CheckCircle className="w-5 h-5" /> : <AlertTriangle className="w-5 h-5" />}
                    <span className="font-medium text-sm">{status.message}</span>
                </div>
            )}

            {/* Content Area */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                {/* Main Content - Markdown Viewer */}
                <div className="lg:col-span-3 glass-card flex flex-col min-h-[500px]">
                    <div className="flex items-center gap-2 p-4 border-b border-white/5 bg-white/5">
                        <FileText className="w-4 h-4 text-gray-400" />
                        <span className="text-xs font-mono text-gray-400 uppercase tracking-widest">Docs/changelog.md</span>
                    </div>

                    <div className="p-6 md:p-10 flex-grow scrollbar-thin overflow-y-auto max-h-[700px]">
                        {loading ? (
                            <div className="flex flex-col items-center justify-center h-full gap-4 text-gray-500">
                                <RefreshCw className="w-12 h-12 animate-spin" />
                                <p className="animate-pulse">Sincronizando documentação...</p>
                            </div>
                        ) : (
                            <div className="prose prose-invert max-w-none 
                                prose-headings:text-neon-green prose-headings:font-bold
                                prose-h1:text-3xl prose-h1:mb-8 prose-h1:border-b prose-h1:border-neon-green/20 prose-h1:pb-4
                                prose-h2:text-xl prose-h2:mt-10 prose-h2:mb-4 prose-h2:flex prose-h2:items-center
                                prose-ul:list-disc prose-li:text-gray-300
                                prose-code:bg-white/10 prose-code:px-1 prose-code:py-0.5 prose-code:rounded prose-code:text-neon-green
                                prose-strong:text-white
                            ">
                                <ReactMarkdown>{changelog}</ReactMarkdown>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AutoDocs;
