// frontend/src/types/modelagem.ts

export interface ProcessoBPMN {
  id: number;
  nome_processo: string;
  descricao: string;
  diagrama_xml_url?: string;
  versao: string;
}

export interface ProcessoBPMNCreate {
  nome_processo: string;
  descricao: string;
  diagrama_xml_url?: string;
  versao: string;
}