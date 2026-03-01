import React, { useEffect, useState, useRef } from 'react';
import { getLogs } from '../services/api';
import { Terminal, Trash2, RefreshCcw } from 'lucide-react';

const AgentTerminal: React.FC = () => {
    const [logs, setLogs] = useState<string[]>([]);
    const [loading, setLoading] = useState(false);
    const scrollRef = useRef<HTMLDivElement>(null);

    const fetchLogs = async () => {
        setLoading(true);
        try {
            const response = await getLogs(100);
            if (response.data && response.data.logs) {
                setLogs(response.data.logs);
            }
        } catch (error) {
            console.error('Failed to fetch logs', error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchLogs();
        const interval = setInterval(fetchLogs, 5000);
        return () => clearInterval(interval);
    }, []);

    useEffect(() => {
        if (scrollRef.current) {
            scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
        }
    }, [logs]);

    return (
        <div className="glass rounded-2xl flex flex-col h-[500px] border-neonCyan/10">
            <div className="p-4 border-b border-white/5 flex justify-between items-center">
                <div className="flex items-center gap-2 text-neonCyan">
                    <Terminal size={18} />
                    <span className="font-bold tracking-tight">AGENT_TERMINAL_V1.0</span>
                </div>
                <div className="flex gap-2">
                    <button onClick={fetchLogs} className="p-2 hover:bg-white/5 rounded-lg text-white/60 transition-colors">
                        <RefreshCcw size={16} className={loading ? 'animate-spin' : ''} />
                    </button>
                    <button onClick={() => setLogs([])} className="p-2 hover:bg-white/5 rounded-lg text-white/60 transition-colors">
                        <Trash2 size={16} />
                    </button>
                </div>
            </div>

            <div
                ref={scrollRef}
                className="flex-1 overflow-y-auto p-4 font-mono text-sm space-y-1 bg-black/20"
            >
                {logs.length === 0 ? (
                    <p className="text-white/20 italic">Aguardando rastro do agente...</p>
                ) : (
                    logs.map((log, i) => (
                        <div key={i} className="flex gap-3">
                            <span className="text-white/20 select-none">{(i + 1).toString().padStart(3, '0')}</span>
                            <span className="text-white/80 break-all">{log}</span>
                        </div>
                    ))
                )}
            </div>

            <div className="p-2 px-4 border-t border-white/5 bg-white/5 flex justify-between items-center text-[10px] text-white/30 uppercase tracking-widest">
                <span>Status: Operational</span>
                <span>Output: stdout</span>
            </div>
        </div>
    );
};

export default AgentTerminal;
