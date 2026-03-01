import React, { useState, useEffect } from 'react';
import { getJobs } from '../services/api';
import { Video, Clock, CheckCircle, AlertCircle, RefreshCw, ExternalLink } from 'lucide-react';

interface Job {
    id: string;
    title?: string;
    status: 'pending' | 'processing' | 'completed' | 'failed';
    created_at: string;
    updated_at: string;
    error?: string;
    metadata?: any;
}

const VideoFactory: React.FC = () => {
    const [jobs, setJobs] = useState<Job[]>([]);
    const [loading, setLoading] = useState(true);
    const [refreshing, setRefreshing] = useState(false);

    const fetchJobs = async () => {
        setRefreshing(true);
        try {
            const response = await getJobs();
            // Ensure we handle both list and object responses if backend varies
            const data = Array.isArray(response.data) ? response.data : Object.values(response.data);
            setJobs(data as Job[]);
        } catch (error) {
            console.error('Failed to fetch jobs', error);
        } finally {
            setLoading(false);
            setRefreshing(false);
        }
    };

    useEffect(() => {
        fetchJobs();
        const interval = setInterval(fetchJobs, 15000); // Polling every 15s
        return () => clearInterval(interval);
    }, []);

    const getStatusIcon = (status: string) => {
        switch (status) {
            case 'completed': return <CheckCircle className="text-neonGreen" size={18} />;
            case 'failed': return <AlertCircle className="text-red-500" size={18} />;
            case 'processing': return <RefreshCw className="text-neonCyan animate-spin" size={18} />;
            default: return <Clock className="text-white/40" size={18} />;
        }
    };

    const getStatusText = (status: string) => {
        switch (status) {
            case 'completed': return <span className="text-neonGreen">COMPLETED</span>;
            case 'failed': return <span className="text-red-500">FAILED</span>;
            case 'processing': return <span className="text-neonCyan">PROCESSING</span>;
            default: return <span className="text-white/40">PENDING</span>;
        }
    };

    if (loading && !refreshing) {
        return (
            <div className="flex items-center justify-center min-h-[400px]">
                <RefreshCw className="text-neonCyan animate-spin" size={32} />
            </div>
        );
    }

    return (
        <div className="flex flex-col gap-6 animate-in fade-in duration-500">
            <div className="flex justify-between items-center">
                <h2 className="text-xl font-bold flex items-center gap-3">
                    <Video className="text-neonCyan" /> JOB_QUEUE
                </h2>
                <button
                    onClick={fetchJobs}
                    disabled={refreshing}
                    className={`p-2 rounded-lg bg-white/5 border border-white/10 hover:border-neonCyan transition-all ${refreshing ? 'opacity-50' : ''}`}
                >
                    <RefreshCw size={18} className={refreshing ? 'animate-spin' : ''} />
                </button>
            </div>

            <div className="glass rounded-2xl overflow-hidden border-white/5">
                <div className="overflow-x-auto">
                    <table className="w-full text-left border-collapse">
                        <thead>
                            <tr className="bg-white/5 text-[10px] font-bold uppercase tracking-widest text-white/40">
                                <th className="px-6 py-4">Status</th>
                                <th className="px-6 py-4">Job ID / Title</th>
                                <th className="px-6 py-4 text-center">Progress</th>
                                <th className="px-6 py-4">Created</th>
                                <th className="px-6 py-4 text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-white/5">
                            {jobs.length === 0 ? (
                                <tr>
                                    <td colSpan={5} className="px-6 py-20 text-center opacity-20">
                                        <p className="text-sm uppercase tracking-widest">No production jobs found</p>
                                    </td>
                                </tr>
                            ) : (
                                jobs.map((job) => (
                                    <tr key={job.id} className="hover:bg-white/[0.02] transition-colors group">
                                        <td className="px-6 py-4">
                                            <div className="flex items-center gap-2 text-[10px] font-bold">
                                                {getStatusIcon(job.status)}
                                                {getStatusText(job.status)}
                                            </div>
                                        </td>
                                        <td className="px-6 py-4">
                                            <div className="flex flex-col">
                                                <span className="text-xs font-mono text-white/60 group-hover:text-neonCyan transition-colors">#{job.id.slice(0, 8)}</span>
                                                <span className="text-sm font-medium">{job.title || 'Untitled Video Production'}</span>
                                            </div>
                                        </td>
                                        <td className="px-6 py-4">
                                            <div className="w-full bg-white/5 h-1 rounded-full overflow-hidden min-w-[100px]">
                                                <div
                                                    className={`h-full transition-all duration-1000 ${job.status === 'completed' ? 'bg-neonGreen w-full' :
                                                            job.status === 'failed' ? 'bg-red-500 w-full' :
                                                                job.status === 'processing' ? 'bg-neonCyan w-[65%]' : 'bg-white/10 w-[10%]'
                                                        }`}
                                                />
                                            </div>
                                        </td>
                                        <td className="px-6 py-4 text-xs text-white/40">
                                            {new Date(job.created_at).toLocaleString()}
                                        </td>
                                        <td className="px-6 py-4 text-right">
                                            <button className="p-2 rounded-lg bg-white/5 hover:bg-neonCyan/20 text-white/40 hover:text-neonCyan transition-all">
                                                <ExternalLink size={16} />
                                            </button>
                                        </td>
                                    </tr>
                                ))
                            )}
                        </tbody>
                    </table>
                </div>
            </div>

            {/* Stats Summary */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="glass p-4 rounded-xl border-white/5">
                    <p className="text-[10px] font-bold text-white/40 uppercase tracking-widest mb-1">Queue Size</p>
                    <p className="text-2xl font-bold">{jobs.length}</p>
                </div>
                <div className="glass p-4 rounded-xl border-white/5">
                    <p className="text-[10px] font-bold text-white/40 uppercase tracking-widest mb-1">Completed</p>
                    <p className="text-2xl font-bold text-neonGreen">{jobs.filter(j => j.status === 'completed').length}</p>
                </div>
                <div className="glass p-4 rounded-xl border-white/5">
                    <p className="text-[10px] font-bold text-white/40 uppercase tracking-widest mb-1">Failed</p>
                    <p className="text-2xl font-bold text-red-500">{jobs.filter(j => j.status === 'failed').length}</p>
                </div>
            </div>
        </div>
    );
};

export default VideoFactory;
