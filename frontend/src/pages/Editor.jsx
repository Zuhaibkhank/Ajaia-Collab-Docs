import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import {
  getDocument,
  updateDocument,
  shareDocument,
} from "../services/documentService";

function Editor() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [shareUser, setShareUser] = useState("");

  useEffect(() => {
    loadDocument();
  }, []);

  const loadDocument = async () => {
    try {
      const doc = await getDocument(id);

      setTitle(doc.title);
      setContent(doc.content);
    } catch (err) {
      alert("Document not found");
    }
  };

  const handleSave = async () => {
    try {
      await updateDocument(id, {
        title,
        content,
      });

      alert("Document Updated");
    } catch (err) {
      alert("Update Failed");
    }
  };

  const handleShare = async () => {
    if (!shareUser) return;

    try {
      await shareDocument(id, Number(shareUser));

      alert("Document Shared");

      setShareUser("");
    } catch (err) {
      alert(
        err.response?.data?.detail ||
          "Share Failed"
      );
    }
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>Document Editor</h1>

      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Title"
        style={{
          width: "100%",
          padding: 10,
          marginBottom: 15,
        }}
      />

      <textarea
        rows={15}
        value={content}
        onChange={(e) => setContent(e.target.value)}
        style={{
          width: "100%",
          padding: 10,
        }}
      />

      <br />
      <br />

      <button onClick={handleSave}>
        Save Changes
      </button>

      <button
        style={{ marginLeft: 10 }}
        onClick={() => navigate("/dashboard")}
      >
        Back
      </button>

      <hr />

      <h2>Share Document</h2>

      <input
        type="number"
        placeholder="User ID (Example: 2)"
        value={shareUser}
        onChange={(e) => setShareUser(e.target.value)}
        style={{
          width: 200,
          padding: 10,
        }}
      />

      <button
        style={{ marginLeft: 10 }}
        onClick={handleShare}
      >
        Share
      </button>
    </div>
  );
}

export default Editor;