// frontend/src/components/ExecucaoManager.tsx

import { useState, useEffect, FormEvent } from 'react';
import api from '../services/api';
import { CasoTesteBDD, CasoTesteBDDCreate } from '../types/execucao';

export function ExecucaoManager() {
  const [testes, setTestes] = useState<CasoTesteBDD[]>([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState<CasoTesteBDDCreate>({
    titulo: '',
    cenario: '',
    dado_que: '',
    quando: '',
    entao: '',
    status: 'Pendente',
  });

  const fetchTestes = async () => {
    try {
      const response = await api.get<CasoTesteBDD[]>('/execucao/testes-bdd/');
      setTestes(response.data);
    } catch (error) {
      console.error('Erro ao buscar casos de teste BDD:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTestes();
  }, []);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/execucao/testes-bdd/', formData);
      setFormData({
        titulo: '',
        cenario: '',
        dado_que: '',
        quando: '',
        entao: '',
        status: 'Pendente',
      });
      await fetchTestes();
    } catch (error) {
      console.error('Erro ao cadastrar caso de teste BDD:', error);
      alert('Falha ao registrar o caso de teste.');
    }
  };

  return (
    <section style={{ marginTop: '2rem', padding: '1rem', border: '1px solid #444', borderRadius: '8px' }}>
      <h2>Módulo 3: Execução e Homologação (Testes BDD)</h2>

      <form onSubmit={handleSubmit} style={{ display: 'grid', gap: '0.8rem', maxWidth: '500px', marginBottom: '1.5rem' }}>
        <input
          type="text"
          placeholder="Título do Teste"
          value={formData.titulo}
          onChange={(e) => setFormData({ ...formData, titulo: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Cenário de Teste"
          value={formData.cenario}
          onChange={(e) => setFormData({ ...formData, cenario: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Dado que... (Pré-condição)"
          value={formData.dado_que}
          onChange={(e) => setFormData({ ...formData, dado_que: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Quando... (Ação)"
          value={formData.quando}
          onChange={(e) => setFormData({ ...formData, quando: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Então... (Resultado esperado)"
          value={formData.entao}
          onChange={(e) => setFormData({ ...formData, entao: e.target.value })}
          required
        />
        <select value={formData.status} onChange={(e) => setFormData({ ...formData, status: e.target.value })}>
          <option value="Pendente">Pendente</option>
          <option value="Em Execução">Em Execução</option>
          <option value="Aprovado">Aprovado</option>
          <option value="Reprovado">Reprovado</option>
        </select>
        <button type="submit">Cadastrar Caso de Teste BDD</button>
      </form>

      <h3>Casos de Teste BDD Registrados</h3>
      {loading ? (
        <p>Carregando cenários de teste...</p>
      ) : testes.length === 0 ? (
        <p>Nenhum teste BDD registrado.</p>
      ) : (
        <ul>
          {testes.map((t) => (
            <li key={t.id} style={{ marginBottom: '1rem' }}>
              <strong>{t.titulo}</strong> - <em>Status: {t.status}</em>
              <p style={{ margin: '0.2rem 0', color: '#ccc' }}>
                <strong>Cenário:</strong> {t.cenario}<br />
                <strong>Dado que</strong> {t.dado_que}<br />
                <strong>Quando</strong> {t.quando}<br />
                <strong>Então</strong> {t.entao}
              </p>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}