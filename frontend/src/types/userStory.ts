// frontend/src/types/userStory.ts

export interface UserStory {
  id: number;
  titulo: string;
  como_um: string;
  eu_quero: string;
  para_que: string;
  criterios_aceite: string;
  pontos: number;
  requisito_id?: number;
}

export interface UserStoryCreate {
  titulo: string;
  como_um: string;
  eu_quero: string;
  para_que: string;
  criterios_aceite: string;
  pontos: number;
  requisito_id?: number;
}