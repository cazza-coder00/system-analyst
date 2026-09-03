// frontend/src/components/StakeholderForm.tsx

import { useState, FormEvent } from 'react';
import api from '../services/api';
import { StakeholderCreate } from '../types/iniciacao';

interface StakeholderFormProps {
  onSuccess: () => void;
}

export function StakeholderForm({ onSuccess }: StakeholderFormProps) {
  const [formData, setFormData] = useState<StakeholderCreate>({
    nome: '',
    cargo: '',
    departamento: '',
    email: '',
  });
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      await api.post('/iniciacao/stakeholders/', formData);
      setFormData({ nome: '', cargo: '', departamento: '', email: '' });
      onSuccess();
    } catch (error) {
      console.error('Erro ao cadastrar stakeholder:', error);
      alert('Falha ao cadastrar. Verifique os dados e tente novamente.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: '2rem', padding: '1rem', border: '1px solid #444', borderRadius: '8px' }}>
      <h3>Cadastrar Novo Stakeholder</h3>
      <div style={{ display: 'grid', gap: '0.8rem', maxWidth: '400px' }}>
        <input
          type="text"
          placeholder="Nome"
          value={formData.nome}
          onChange={(e) => setFormData({ ...formData, nome: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Cargo"
          value={formData.cargo}
          onChange={(e) => setFormData({ ...formData, cargo: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Departamento"
          value={formData.departamento}
          onChange={(e) => setFormData({ ...formData, departamento: e.target.value })}
          required
        />
        <input
          type="email"
          placeholder="E-mail"
          value={formData.email}
          onChange={(e) => setFormData({ ...formData, email: e.target.value })}
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Salvando...' : 'Cadastrar Stakeholder'}
        </button>
      </div>
    </form>
  );
}