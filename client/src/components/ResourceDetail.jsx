import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const ResourceDetail = () => {
    const { pathId, moduleId, resourceId } = useParams();
    const [resource, setResource] = useState(null);

    useEffect(() => {
        fetch(`/learning-paths/${pathId}/module/${moduleId}/resource/${resourceId}`)
            .then(res => res.json())
            .then(data => setResource(data))
            .catch(error => console.error('Error fetching resource details:', error));
    }, [pathId, moduleId, resourceId]);

    if (!resource) return <p>Loading resource...</p>;

    return (
        <div>
            <h2>{resource.title}</h2>
            <p>Type: {resource.type}</p>
            <a href={resource.link} target="_blank" rel="noopener noreferrer">Open Resource</a>
        </div>
    );
};

export default ResourceDetail;
