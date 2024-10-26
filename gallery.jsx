import React, { useState } from 'react';
import { LazyLoadImage } from 'react-lazy-load-image-component';
import Modal from '../common/Modal';
import './Gallery.css';

const Gallery = ({ images }) => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [filter, setFilter] = useState('all');

  const filteredImages = images.filter(image => 
    filter === 'all' ? true : image.category === filter
  );

  return (
    <div className="gallery">
      <div className="gallery-filters">
        <button onClick={() => setFilter('all')}>All</button>
        <button onClick={() => setFilter('paintings')}>Paintings</button>
        <button onClick={() => setFilter('digital')}>Digital</button>
      </div>
      
      <div className="gallery-grid">
        {filteredImages.map(image => (
          <div 
            key={image.id} 
            className="gallery-item"
            onClick={() => setSelectedImage(image)}
          >
            <LazyLoadImage
              src={image.thumbnail}
              alt={image.title}
              effect="blur"
            />
            <div className="gallery-item-info">
              <h3>{image.title}</h3>
              <p>{image.description}</p>
            </div>
          </div>
        ))}
      </div>

      {selectedImage && (
        <Modal onClose={() => setSelectedImage(null)}>
          <img 
            src={selectedImage.fullSize} 
            alt={selectedImage.title} 
          />
          <h2>{selectedImage.title}</h2>
          <p>{selectedImage.description}</p>
          <div className="social-share">
            {/* Add social share buttons */}
          </div>
        </Modal>
      )}
    </div>
  );
};

export default Gallery;
