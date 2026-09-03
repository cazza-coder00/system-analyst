// frontend/src/components/RequisitosManager.tsx

import { useState, useEffect, FormEvent } from 'react';
import api from '../services/api';
import { Requisito, RequisitoCreate } from '../types/requisito';

export function RequisitosManager() {
  const [requisitos, setRequisitos] = useState<Requisito[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [formData, setFormData] = useState<RequisitoCreate>({
    codigo: '',
    titulo: '',
    descricao: '',
    tipo: 'Funcional',
    prioridade: 'Alta',
  });

  const carregarRequisitos = async () => {
    try {
      const response = await api.get<Requisito[]>('/iniciacao/requisitos/');
      setRequisitos(response.data);
    } catch (error) {
      console.error('Erro ao carregar requisitos:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    carregarRequisitos();
  }, []);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/iniciacao/requisitos/', formData);
      setFormData({ codigo: '', titulo: '', descricao: '', tipo: 'Funcional', prioridade: 'Alta' });
      await carregarRequisitos();
    } catch (error) {
      console.error('Erro ao cadastrar requisito:', error);
      alert('Falha ao cadastrar requisito.');
    }
  };

  return (
    <section style={{ marginTop: '2rem', padding: '1rem', border: '1px solid #444', borderRadius: '8px' }}>
      <h2>Módulo 1: Levantamento de Requisitos</h2>

      <form onSubmit={handleSubmit} style={{ display: 'grid', gap: '0.8rem', maxWidth: '500px', marginBottom: '1.5rem' }}>
        <input
          type="text"
          placeholder="Código (ex: RF-001)"
          value={formData.codigo}
          onChange={(e) => setFormData({ ...formData, codigo: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Título do Requisito"
          value={formData.titulo}
          onChange={(e) => setFormData({ ...formData, titulo: e.target.value })}
          required
        />
        <textarea
          placeholder="Descrição detalhada"
          value={formData.descricao}
          onChange={(e) => setFormData({ ...formData, descricao: e.target.value })}
          required
        />
        <select value={formData.tipo} onChange={(e) => setFormData({ ...formData, tipo: e.target.value })}>
          <option value="Funcional">Funcional</option>
          <option value="Não-Funcional">Não-Funcional</option>
        </select>
        <select value={formData.prioridade} onChange={(e) => setFormData({ ...formData, prioridade: e.target.value })}>
          <option value="Alta">Alta</option>
          <option value="Média">Média</option>
          <option value="Baixa">Baixa</option>
        </select>
        <button type="submit">Cadastrar Requisito</button>
      </form>

      <h3>Requisitos Mapeados</h3>
      {loading ? (
        <p>Carregando requisitos...</p>
      ) : requisitos.length === 0 ? (
        <p>Nenhum requisito cadastrado.</p>
      ) : (
        <ul>
          {requisitos.map((req) => (
            <li key={req.id} style={{ marginBottom: '0.8rem' }}>
              <strong>[{req.codigo}] {req.titulo}</strong> ({req.tipo} - Prioridade {req.prioridade})
              <p style={{ margin: '0.2rem 0 0 0', color: '#ccc' }}>{req.descricao}</p>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}