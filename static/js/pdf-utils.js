function loadImg(src, opacity) {
  return new Promise(resolve => {
    const img = new Image(); img.crossOrigin = 'anonymous';
    img.onload = () => {
      const c = document.createElement('canvas');
      c.width = img.naturalWidth || 300; c.height = img.naturalHeight || 300;
      const ctx = c.getContext('2d');
      if (opacity != null && opacity < 1) ctx.globalAlpha = opacity;
      ctx.drawImage(img, 0, 0); resolve(c.toDataURL('image/png'));
    };
    img.onerror = () => resolve(null); img.src = src;
  });
}

function loadLogo(src) {
  return new Promise(resolve => {
    const img = new Image(); img.crossOrigin = 'anonymous';
    img.onload = () => {
      const c = document.createElement('canvas');
      c.width = img.naturalWidth || 300; c.height = img.naturalHeight || 300;
      const ctx = c.getContext('2d'); ctx.drawImage(img, 0, 0);
      resolve({ url: c.toDataURL('image/png'), w: img.naturalWidth || 300, h: img.naturalHeight || 300 });
    };
    img.onerror = () => resolve(null); img.src = src;
  });
}

function logoDims(logo, targetH) {
  if (!logo) return { w: targetH, h: targetH };
  return { w: Math.round((logo.w / logo.h) * targetH * 10) / 10, h: targetH };
}
