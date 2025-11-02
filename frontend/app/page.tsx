"use client";
import { useState, useEffect } from "react";
import axios from "axios";

interface Task {
  id: number;
  title: string;
}

export default function Home() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [title, setTitle] = useState<string>("");

  useEffect(() => {
    axios.get<Task[]>("http://localhost:8000/api/tasks").then((res) => setTasks(res.data));
  }, []);

  const addTask = async () => {
    const res = await axios.post<Task>(`http://localhost:8000/api/tasks?title=${title}`);
    setTasks([...tasks, res.data]);
    setTitle("");
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Cloud Task Manager</h1>
      <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="New task..." />
      <button onClick={addTask}>Add</button>
      <ul>{tasks.map((t) => <li key={t.id}>{t.title}</li>)}</ul>
    </div>
  );
}