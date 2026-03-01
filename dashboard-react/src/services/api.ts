import axios from 'axios';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
    timeout: 10000,
});

export const getHealth = () => api.get('/maintenance/health');
export const getAgentStatus = () => api.get('/agent/status');
export const getLogs = (lines: number = 50) => api.get(`/maintenance/logs?lines=${lines}`);
export const getJobs = () => api.get('/jobs');
export const getChangelog = () => api.get('/maintenance/docs/changelog');
export const runAutoDocs = () => api.post('/agent/run/tool_auto_docs');
export const triggerHeal = () => api.post('/maintenance/heal');
export const getAgentLogs = () => api.get('/maintenance/logs?lines=100');
export const getConfig = () => api.get('/maintenance/config');
export const updateConfig = (config: any) => api.post('/maintenance/config', config);

export default api;
