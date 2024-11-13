import React, { useState } from 'react';

function CreateLearningPathForm({ onSubmit }) {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    modules: [{ title: '', description: '', resources: [] }],
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleAddModule = () => {
    setFormData({
      ...formData,
      modules: [...formData.modules, { title: '', description: '', resources: [] }],
    });
  };

  const handleModuleChange = (index, field, value) => {
    const updatedModules = formData.modules.map((module, idx) =>
      idx === index ? { ...module, [field]: value } : module
    );
    setFormData({ ...formData, modules: updatedModules });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await fetch('/api/create_path', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      alert("Learning path created successfully!");
    } catch (error) {
      console.error("Error creating path:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="title"
        placeholder="Path Title"
        value={formData.title}
        onChange={handleInputChange}
      />
      <textarea
        name="description"
        placeholder="Path Description"
        value={formData.description}
        onChange={handleInputChange}
      />
      <h3>Modules</h3>
      {formData.modules.map((module, index) => (
        <div key={index}>
          <input
            type="text"
            placeholder="Module Title"
            value={module.title}
            onChange={(e) => handleModuleChange(index, 'title', e.target.value)}
          />
          <textarea
            placeholder="Module Description"
            value={module.description}
            onChange={(e) => handleModuleChange(index, 'description', e.target.value)}
          />
        </div>
      ))}
      <button type="button" onClick={handleAddModule}>Add Module</button>
      <button type="submit">Create Learning Path</button>
    </form>
  );
}

export default CreateLearningPathForm;
