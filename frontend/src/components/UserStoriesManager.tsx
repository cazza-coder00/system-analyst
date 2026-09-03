// frontend/src/components/UserStoriesManager.tsx

import { useState, useEffect, FormEvent } from 'react';
import api from '../services/api';
import { UserStory, UserStoryCreate } from '../types/userStory';

export function UserStoriesManager() {
  const [stories, setStories] = useState<UserStory[]>([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState<UserStoryCreate>({
    titulo: '',
    como_um: '',
    eu_quero: '',
    para_que: '',
    criterios_aceite: '',
    pontos: 1,
  });

  const fetchStories = async () => {
    try {
      const response = await api.get<UserStory[]>('/iniciacao/user-stories/');
      setStories(response.data);
    } catch (error) {
      console.error('Erro ao buscar histórias de usuário:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStories();
  }, []);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/iniciacao/user-stories/', formData);
      setFormData({
        titulo: '',
        como_um: '',
        eu_quero: '',
        para_que: '',
        criterios_aceite: '',
        pontos: 1,
      });
      await fetchStories();
    } catch (error) {
      console.error('Erro ao cadastrar User Story:', error);
      alert('Falha ao cadastrar a história de usuário.');
    }
  };

  return (
    <section style={{ marginTop: '2rem', padding: '1rem', border: '1px solid #444', borderRadius: '8px' }}>
      <h2>Módulo 1: User Stories (Histórias de Usuário)</h2>

      <form onSubmit={handleSubmit} style={{ display: 'grid', gap: '0.8rem', maxWidth: '500px', marginBottom: '1.5rem' }}>
        <input
          type="text"
          placeholder="Título da História"
          value={formData.titulo}
          onChange={(e) => setFormData({ ...formData, titulo: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Como um... (Ator)"
          value={formData.como_um}
          onChange={(e) => setFormData({ ...formData, como_um: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Eu quero... (Ação)"
          value={formData.eu_quero}
          onChange={(e) => setFormData({ ...formData, eu_quero: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Para que... (Benefício)"
          value={formData.para_que}
          onChange={(e) => setFormData({ ...formData, para_que: e.target.value })}
          required
        />
        <textarea
          placeholder="Critérios de Aceite"
          value={formData.criterios_aceite}
          onChange={(e) => setFormData({ ...formData, criterios_aceite: e.target.value })}
        />
        <input
          type="number"
          placeholder="Pontuação"
          value={formData.pontos}
          onChange={(e) => setFormData({ ...formData, pontos: Number(e.target.value) })}
          min="1"
        />
        <button type="submit">Cadastrar User Story</button>
      </form>

      <h3>User Stories Mapeadas</h3>
      {loading ? (
        <p>Carregando histórias...</p>
      ) : stories.length === 0 ? (
        <p>Nenhuma User Story cadastrada.</p>
      ) : (
        <ul>
          {stories.map((us) => (
            <li key={us.id} style={{ marginBottom: '1rem' }}>
              <strong>{us.titulo}</strong> ({us.pontos} pts)
              <p style={{ margin: '0.2rem 0', color: '#ccc' }}>
                <strong>Como</strong> {us.como_um}, <strong>quero</strong> {us.eu_quero} <strong>para que</strong> {us.para_que}.
              </p>
              {us.criterios_aceite && (
                <small style={{ color: '#aaa' }}>Critérios: {us.criterios_aceite}</small>
              )}
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}