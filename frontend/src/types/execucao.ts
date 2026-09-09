// frontend/src/types/execucao.ts

export interface CasoTesteBDD {
  id: number;
  titulo: string;
  cenario: string;
  dado_que: string;
  quando: string;
  entao: string;
  status: string;
  user_story_id?: number;
}

export interface CasoTesteBDDCreate {
  titulo: string;
  cenario: string;
  dado_que: string;
  quando: string;
  entao: string;
  status: string;
  user_story_id?: number;
}