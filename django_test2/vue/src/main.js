import Vue from 'vue'
import Tree from './views/Tree'
import './plugins/element.js'
import './style/theme.scss'

Vue.config.productionTip = false;

new Vue({
  render: h => h(Tree)
}).$mount('#app');
