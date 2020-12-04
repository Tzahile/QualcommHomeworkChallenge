import axios from "axios";
export async function UpdateVersion(card) {
  return axios.put(`/versions/${card.id}`, { notes: card.notes });
}

export async function DeleteVersion(card) {
  return axios.delete(`/versions/${card.id}`);
}

export async function CreateVersion(card) {
  return axios.post(`/versions/${card.id}`, { ...card });
}
