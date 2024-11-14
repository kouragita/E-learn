import React from 'react';
import { useParams } from 'react-router-dom';
import ModuleDetail from './ModuleDetail';

function LearningPathDetail() {
  const { pathId } = useParams();
  
  return <div>
    <h2>Details of Learning Path by id {pathId}</h2>
    <ModuleDetail/>
    </div>;
}

export default LearningPathDetail;
