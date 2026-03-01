import React, { useState, useEffect } from 'react';
import StatsCard from './StatsCard';
import { Database, HardDrive, ShieldCheck, Activity } from 'lucide-react';
import { getHealth, getAgentStatus } from '../services/api';

const HealthGrid: React.FC = () => {
    const [health, setHealth] = useState<any>(null);
    const [agent, setAgent] = useState<any>(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const [hRes, aRes] = await Promise.all([getHealth(), getAgentStatus()]);
                setHealth(hRes.data);
                setAgent(aRes.data);
            } catch (error) {
                console.error('Failed to fetch health data', error);
            }
        };

        fetchData();
        const interval = setInterval(fetchData, 10000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <StatsCard
                title="Ollama Availability"
                value={agent?.ollama_available ? 'ONLINE' : 'OFFLINE'}
                icon={<Activity />}
                color={agent?.ollama_available ? 'green' : 'cyan'}
                trend="IA ENGINE"
            />
            <StatsCard
                title="Database Status"
                value={health?.components?.database === 'connected' ? 'CONNECTED' : 'DISCONNECTED'}
                icon={<Database />}
                color={health?.components?.database === 'connected' ? 'green' : 'cyan'}
                trend="POSTGRES"
            />
            <StatsCard
                title="Disk Space"
                value={health?.components?.disk?.free_gb ? `${health.components.disk.free_gb} GB` : 'N/A'}
                icon={<HardDrive />}
                color="blue"
                trend="STORAGE"
            />
            <StatsCard
                title="Sentinel Status"
                value={agent?.running ? 'ACTIVE' : 'IDLE'}
                icon={<ShieldCheck />}
                color="green"
                trend="AUTO-HEALING"
            />
        </div>
    );
};

export default HealthGrid;
