import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import ResourceDetail from './ResourceDetail';
import QuizDetail from './QuizDetail';

const ModuleDetail = () => {
    const { pathId, moduleId } = useParams();
    const [module, setModule] = useState(null);
    const [resources, setResources] = useState([]);

    useEffect(() => {
        fetch(`/learning-paths/${pathId}/module/${moduleId}`)
            .then(res => res.json())
            .then(data => setModule(data))
            .catch(error => console.error('Error fetching module details:', error));

        fetch(`/learning-paths/${pathId}/module/${moduleId}/resources`)
            .then(res => res.json())
            .then(data => setResources(data.resources))
            .catch(error => console.error('Error fetching resources:', error));
    }, [pathId, moduleId]);

    if (!module) return <p>Loading module...</p>;

    return (
        <div>
            <h2>{module.title}</h2>
            <p>{module.description}</p>
            <ResourceDetail resources={resources} />
            <QuizDetail/>
        </div>
    );
};

export default ModuleDetail;
