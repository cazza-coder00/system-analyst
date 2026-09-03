// frontend/src/types/requisito.ts

export interface Requisito {
  id: number;
  codigo: string;
  titulo: string;
  descricao: string;
  tipo: string;
  prioridade: string;
}

export interface RequisitoCreate {
  codigo: string;
  titulo: string;
  descricao: string;
  tipo: string;
  prioridade: string;
}