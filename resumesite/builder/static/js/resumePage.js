document.getElementById('download').addEventListener('click', () => {
  const resume = document.getElementById('inner');
  
  html2pdf(resume, {
      margin: 0,
      filename: 'resume.pdf',
      image: { type: 'jpeg', quality: 0.98 },
      html2canvas: { scale: 2 },
      jsPDF: { unit: 'cm', format: 'a4', orientation: 'portrait' }
  });
});
