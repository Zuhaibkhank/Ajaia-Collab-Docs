import api from "./api";

export const getDocuments = async () => {
  const res = await api.get("/documents");
  return res.data;
};

export const getDocument = async (id) => {
  const res = await api.get(`/documents/${id}`);
  return res.data;
};

export const createDocument = async (data) => {
  const res = await api.post("/documents", data);
  return res.data;
};

export const updateDocument = async (id, data) => {
  const res = await api.put(`/documents/${id}`, data);
  return res.data;
};

export const deleteDocument = async (id) => {
  const res = await api.delete(`/documents/${id}`);
  return res.data;
};

export const shareDocument = async (id, user_id) => {
  const res = await api.post(`/documents/${id}/share`, {
    user_id,
  });

  return res.data;
};

export const sharedDocuments = async () => {
  const res = await api.get("/documents/shared/me");
  return res.data;
};