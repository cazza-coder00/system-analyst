// frontend/src/App.tsx

import { useState } from 'react';
import { StakeholderForm } from './components/StakeholderForm';
import { StakeholdersList } from './components/StakeholdersList';
import { RequisitosManager } from './components/RequisitosManager';
import { UserStoriesManager } from './components/UserStoriesManager';

function App() {
  const [refreshKey, setRefreshKey] = useState(0);

  return (
    <main style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>Sistema de Análise de Negócios</h1>
      <hr style={{ marginBottom: '1.5rem' }} />
      <StakeholderForm onSuccess={() => setRefreshKey((prev) => prev + 1)} />
      <StakeholdersList key={refreshKey} />
      <RequisitosManager />
      <UserStoriesManager />
    </main>
  );
}

export default App;