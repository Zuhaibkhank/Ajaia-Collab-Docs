import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  getDocuments,
  createDocument,
  deleteDocument,
  sharedDocuments,
} from "../services/documentService";

function Dashboard() {
  const navigate = useNavigate();

  const [documents, setDocuments] = useState([]);
  const [shared, setShared] = useState([]);

  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const loadDocuments = async () => {
    try {
      const data = await getDocuments();
      setDocuments(data);

      const share = await sharedDocuments();
      setShared(share);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    loadDocuments();
  }, []);

  const handleCreate = async () => {
    if (!title || !content) return;

    await createDocument({
      title,
      content,
    });

    setTitle("");
    setContent("");

    loadDocuments();
  };

  const handleDelete = async (id) => {
    if (!window.confirm("Delete document?")) return;

    await deleteDocument(id);

    loadDocuments();
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>Ajaia Collaborative Docs</h1>

      <hr />

      <h2>Create Document</h2>

      <input
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        style={{
          width: "100%",
          padding: 10,
          marginBottom: 10,
        }}
      />

      <textarea
        rows={5}
        placeholder="Content"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        style={{
          width: "100%",
          padding: 10,
        }}
      />

      <br />
      <br />

      <button onClick={handleCreate}>
        Create Document
      </button>

      <hr />

      <h2>My Documents</h2>

      {documents.map((doc) => (
        <div
          key={doc.id}
          style={{
            border: "1px solid #ddd",
            padding: 15,
            marginBottom: 15,
          }}
        >
          <h3>{doc.title}</h3>

          <p>{doc.content}</p>

          <button
            onClick={() =>
              navigate(`/editor/${doc.id}`)
            }
          >
            Edit
          </button>

          <button
            onClick={() => handleDelete(doc.id)}
            style={{ marginLeft: 10 }}
          >
            Delete
          </button>
        </div>
      ))}

      <hr />

      <h2>Shared With Me</h2>

      {shared.map((doc) => (
        <div
          key={doc.id}
          style={{
            border: "1px solid #ddd",
            padding: 15,
            marginBottom: 15,
          }}
        >
          <h3>{doc.title}</h3>

          <p>{doc.content}</p>
        </div>
      ))}
    </div>
  );
}

export default Dashboard;