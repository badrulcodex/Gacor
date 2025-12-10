
(function () {
  const urls = [
    "https://www.effectivegatecpm.com/ztf3zuiy?key=30617628fe35bee9bea93026385e6f17",
    "https://www.effectivegatecpm.com/w4deur4mzh?key=f9741a58a274f0182a88f1ff37734bd9",
    "https://www.effectivegatecpm.com/w4deur4mzh?key=f9741a58a274f0182a88f1ff37734bd9"
  ];

  let index = 0;

  function openNextTab() {
    const url = urls[index];
    window.open(url, '_blank');
    console.log(`Opened: ${url}`);
    index = (index + 1) % urls.length;
  }

  window.onload = () => {
    openNextTab();  
    setInterval(openNextTab, 10000);  
  };
})();