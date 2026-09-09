// frontend/src/components/ModelagemManager.tsx

import { useState, useEffect, FormEvent } from 'react';
import api from '../services/api';
import { ProcessoBPMN, ProcessoBPMNCreate } from '../types/modelagem';

export function ModelagemManager() {
  const [processos, setProcessos] = useState<ProcessoBPMN[]>([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState<ProcessoBPMNCreate>({
    nome_processo: '',
    descricao: '',
    diagrama_xml_url: '',
    versao: '1.0',
  });

  const fetchProcessos = async () => {
    try {
      const response = await api.get<ProcessoBPMN[]>('/modelagem/processos/');
      setProcessos(response.data);
    } catch (error) {
      console.error('Erro ao buscar processos BPMN:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProcessos();
  }, []);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/modelagem/processos/', formData);
      setFormData({ nome_processo: '', descricao: '', diagrama_xml_url: '', versao: '1.0' });
      await fetchProcessos();
    } catch (error) {
      console.error('Erro ao cadastrar processo:', error);
      alert('Falha ao registrar o processo BPMN.');
    }
  };

  return (
    <section style={{ marginTop: '2rem', padding: '1rem', border: '1px solid #444', borderRadius: '8px' }}>
      <h2>Módulo 2: Modelagem e Especificação (BPMN)</h2>

      <form onSubmit={handleSubmit} style={{ display: 'grid', gap: '0.8rem', maxWidth: '500px', marginBottom: '1.5rem' }}>
        <input
          type="text"
          placeholder="Nome do Processo (ex: Mapeamento de Compra)"
          value={formData.nome_processo}
          onChange={(e) => setFormData({ ...formData, nome_processo: e.target.value })}
          required
        />
        <textarea
          placeholder="Descrição do fluxo de trabalho"
          value={formData.descricao}
          onChange={(e) => setFormData({ ...formData, descricao: e.target.value })}
          required
        />
        <input
          type="url"
          placeholder="URL / Link do Diagrama BPMN (opcional)"
          value={formData.diagrama_xml_url}
          onChange={(e) => setFormData({ ...formData, diagrama_xml_url: e.target.value })}
        />
        <input
          type="text"
          placeholder="Versão (ex: 1.0)"
          value={formData.versao}
          onChange={(e) => setFormData({ ...formData, versao: e.target.value })}
          required
        />
        <button type="submit">Cadastrar Processo BPMN</button>
      </form>

      <h3>Processos BPMN Registrados</h3>
      {loading ? (
        <p>Carregando processos...</p>
      ) : processos.length === 0 ? (
        <p>Nenhum processo mapeado até o momento.</p>
      ) : (
        <ul>
          {processos.map((p) => (
            <li key={p.id} style={{ marginBottom: '0.8rem' }}>
              <strong>{p.nome_processo}</strong> (v{p.versao})
              <p style={{ margin: '0.2rem 0', color: '#ccc' }}>{p.descricao}</p>
              {p.diagrama_xml_url && (
                <a href={p.diagrama_xml_url} target="_blank" rel="noreferrer" style={{ color: '#4da6ff' }}>
                  Visualizar Diagrama
                </a>
              )}
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}