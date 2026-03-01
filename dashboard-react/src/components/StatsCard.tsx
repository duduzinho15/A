import React from 'react';
import { motion } from 'framer-motion';

interface StatsCardProps {
    title: string;
    value: string | number;
    icon: React.ReactNode;
    color?: string;
    trend?: string;
}

const StatsCard: React.FC<StatsCardProps> = ({ title, value, icon, color = 'cyan', trend }) => {
    const glowClass = {
        cyan: 'shadow-[0_0_15px_rgba(0,243,255,0.3)] border-neonCyan/20',
        green: 'shadow-[0_0_15px_rgba(57,255,20,0.3)] border-neonGreen/20',
        blue: 'shadow-[0_0_15px_rgba(0,71,255,0.3)] border-neonBlue/20',
    }[color];

    const textClass = {
        cyan: 'text-neonCyan',
        green: 'text-neonGreen',
        blue: 'text-neonBlue',
    }[color];

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={`glass p-6 rounded-2xl flex flex-col gap-4 relative overflow-hidden ${glowClass}`}
        >
            <div className="flex justify-between items-start">
                <div className={`p-3 rounded-xl bg-white/5 ${textClass}`}>
                    {icon}
                </div>
                {trend && (
                    <span className="text-xs font-medium text-white/40 uppercase tracking-wider">
                        {trend}
                    </span>
                )}
            </div>

            <div>
                <p className="text-sm font-medium text-white/50">{title}</p>
                <h3 className={`text-2xl font-bold mt-1 ${textClass}`}>{value}</h3>
            </div>

            <div className="absolute top-0 right-0 w-32 h-32 bg-gradient-to-br from-white/5 to-transparent rounded-full -mr-16 -mt-16 pointer-events-none" />
        </motion.div>
    );
};

export default StatsCard;
