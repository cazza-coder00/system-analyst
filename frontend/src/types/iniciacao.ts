// frontend/src/types/iniciacao.ts

export interface Stakeholder {
  id: number;
  nome: string;
  cargo: string;
  departamento: string;
  email: string;
}

export interface StakeholderCreate {
  nome: string;
  cargo: string;
  departamento: string;
  email: string;
}