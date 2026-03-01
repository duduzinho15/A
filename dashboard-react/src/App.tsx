import { useState } from 'react';
import HealthGrid from './components/HealthGrid';
import AgentTerminal from './components/AgentTerminal';
import VideoFactory from './components/VideoFactory';
import AutoDocs from './components/AutoDocs';
import DebugHeal from './components/DebugHeal';
import SystemSettings from './components/SystemSettings';


import { LayoutDashboard, Settings, Video, FileText, Bug, Activity, Terminal } from 'lucide-react';

function App() {
  const [activeView, setActiveView] = useState<'dashboard' | 'video' | 'docs' | 'debug' | 'settings'>('dashboard');
  const [lastAction, setLastAction] = useState<string | null>(null);

  const handleAction = (action: string) => {
    setLastAction(action);
    console.log(`Executing Action: ${action}`);
    setTimeout(() => setLastAction(null), 3000);
  };

  const navItems = [
    { id: 'dashboard', icon: LayoutDashboard, label: 'Dashboard' },
    { id: 'video', icon: Video, label: 'Video Factory' },
    { id: 'docs', icon: FileText, label: 'Auto-Docs' },
    { id: 'debug', icon: Bug, label: 'Debug/Heal' },
    { id: 'settings', icon: Settings, label: 'System Settings' },
  ] as const;

  const renderContent = () => {
    switch (activeView) {
      case 'dashboard':
        return (
          <div className="flex flex-col gap-8">
            <HealthGrid />

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
              <div className="lg:col-span-2">
                <AgentTerminal />
              </div>

              <div className="flex flex-col gap-6">
                <div className="glass p-6 rounded-2xl border-neonBlue/10">
                  <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
                    <Activity className="text-neonBlue" /> Quick Actions
                  </h3>
                  <div className="grid grid-cols-2 gap-3">
                    <button onClick={() => handleAction('RUN_AUDIT')} className="p-3 rounded-xl bg-white/5 hover:bg-white/10 text-[10px] font-bold transition-all border border-white/5 hover:border-neonCyan text-white/70 hover:text-white">RUN_AUDIT</button>
                    <button onClick={() => handleAction('CLEAR_CACHE')} className="p-3 rounded-xl bg-white/5 hover:bg-white/10 text-[10px] font-bold transition-all border border-white/5 hover:border-white/20 text-white/70 hover:text-white">CLEAR_CACHE</button>
                    <button onClick={() => handleAction('SYNC_RSS')} className="p-3 rounded-xl bg-white/5 hover:bg-white/10 text-[10px] font-bold transition-all border border-white/5 hover:border-neonGreen text-white/70 hover:text-white">SYNC_RSS</button>
                    <button onClick={() => handleAction('RESTART_AI')} className="p-3 rounded-xl bg-white/5 hover:bg-white/10 text-[10px] font-bold transition-all border border-white/5 hover:border-white/20 text-white/70 hover:text-white">RESTART_AI</button>
                  </div>
                </div>

                <div className="glass p-6 rounded-2xl border-neonCyan/10 flex-1">
                  <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
                    <Terminal className="text-neonCyan" /> Active Jobs
                  </h3>
                  <div className="flex flex-col items-center justify-center h-full py-10 opacity-20">
                    <Activity size={48} className="mb-2" />
                    <p className="text-xs uppercase tracking-widest">No active background jobs</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        );
      case 'video':
        return <VideoFactory />;
      case 'docs':
        return <AutoDocs />;
      case 'debug':
        return <DebugHeal />;
      case 'settings':
        return <SystemSettings />;


      default:
        return (
          <div className="flex flex-col items-center justify-center min-h-[60vh] glass rounded-3xl border-white/5">
            <div className="w-20 h-20 rounded-full bg-neonCyan/10 flex items-center justify-center mb-6 text-neonCyan animate-pulse">
              {navItems.find(i => i.id === activeView)?.icon && <Activity size={40} />}
            </div>
            <h2 className="text-2xl font-bold uppercase tracking-widest">{(activeView as string).replace('_', ' ')}</h2>
            <p className="text-white/40 mt-2">Functional module integration coming soon.</p>
            <button
              onClick={() => setActiveView('dashboard')}
              className="mt-8 px-6 py-2 rounded-full border border-neonCyan/30 text-neonCyan text-xs font-bold hover:bg-neonCyan hover:text-background transition-all"
            >
              RETURN TO DASHBOARD
            </button>
          </div>
        );
    }
  };

  return (
    <div className="min-h-screen w-full bg-background text-white font-sans selection:bg-neonCyan/30">
      {/* Sidebar Overlay */}
      <div className="fixed left-0 top-0 h-full w-20 flex flex-col items-center py-8 gap-10 border-r border-white/5 glass z-20">
        <div
          onClick={() => setActiveView('dashboard')}
          className={`w-12 h-12 rounded-xl flex items-center justify-center transition-all cursor-pointer ${activeView === 'dashboard'
            ? 'bg-neonCyan text-background shadow-[0_0_20px_rgba(0,243,255,0.4)]'
            : 'bg-white/5 text-white/40 hover:bg-white/10'
            }`}
        >
          <LayoutDashboard size={24} />
        </div>

        <nav className="flex flex-col gap-6">
          {navItems.filter(item => item.id !== 'dashboard').map((item) => (
            <button
              key={item.id}
              onClick={() => setActiveView(item.id)}
              className={`p-2 rounded-lg transition-all ${activeView === item.id
                ? 'text-neonCyan bg-neonCyan/10 shadow-[0_0_10px_rgba(0,243,255,0.2)]'
                : 'text-white/40 hover:text-neonCyan'
                }`}
              title={item.label}
            >
              <item.icon size={24} />
            </button>
          ))}
        </nav>
      </div>

      {/* Main Content */}
      <main className="pl-24 pr-8 py-8 w-full">
        {/* Header */}
        <header className="flex justify-between items-center mb-12">
          <div>
            <h1 className="text-3xl font-bold tracking-tighter">CONTENT_<span className="text-neonCyan">FACTORY</span></h1>
            <p className="text-white/40 text-sm mt-1 uppercase tracking-widest font-medium">Dashboard v2.0 // {activeView}</p>
          </div>

          <div className="flex items-center gap-4">
            {lastAction && (
              <div className="flex items-center gap-2 px-4 py-2 rounded-full glass border-neonCyan/20 animate-bounce">
                <span className="text-[10px] font-bold text-neonCyan uppercase tracking-widest">Action: {lastAction}</span>
              </div>
            )}
            <div className="flex items-center gap-2 px-4 py-2 rounded-full glass border-neonGreen/20">
              <div className="w-2 h-2 rounded-full bg-neonGreen animate-pulse shadow-[0_0_8px_#39ff14]" />
              <span className="text-[10px] font-bold text-neonGreen uppercase tracking-widest">System Online</span>
            </div>
          </div>
        </header>

        {renderContent()}
      </main>
    </div>
  );
}

export default App;
