// frontend/src/App.tsx

import { useState } from 'react';
import { StakeholderForm } from './components/StakeholderForm';
import { StakeholdersList } from './components/StakeholdersList';

function App() {
  const [refreshKey, setRefreshKey] = useState(0);

  const handleStakeholderAdded = () => {
    setRefreshKey((prev) => prev + 1);
  };

  return (
    <main style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>Sistema de Análise de Negócios</h1>
      <hr style={{ marginBottom: '1.5rem' }} />
      <StakeholderForm onSuccess={handleStakeholderAdded} />
      <StakeholdersList key={refreshKey} />
    </main>
  );
}

export default App;