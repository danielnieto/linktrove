(function(){

const dataQueue = [];

function alpineData(name, func){
  if (!window.Alpine) {
      dataQueue.push({name, func});
      return;
  }

  window.Alpine.data(name, func);
}

function alpineInitListener() {
    while (dataQueue.length) {
      const { name, func } = dataQueue.shift();
      Alpine.data(name, func);
    }

    document.removeEventListener('alpine:init', alpineInitListener);
}

document.addEventListener('alpine:init', alpineInitListener);
window.AlpineData = alpineData;

})();
