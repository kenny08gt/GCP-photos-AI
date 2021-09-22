import { createApp } from 'vue';
import MasonryWall from '@yeger/vue-masonry-wall';
import App from './App.vue';
import router from './router';
import './index.css';

createApp(App).use(router).use(MasonryWall).mount('#app');
