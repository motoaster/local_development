import './bootstrap';
// Vue
import { createApp } from "vue";
import ExampleComponent from './components/exampleComponent.vue';

const app = createApp(ExampleComponent);
app.mount('#app');
