import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      alias: "/gallery",
      name: "gallery",
      component: () => import("./views/Gallery")
    }
  ]
});
