<template>
  <div class="flex main-container" style="height: 100%; margin: 0;">
    <Header />
    <div class="flex-1 overflow-auto">
      <router-view />
    </div>
    <Footer />
  </div>
</template>

<style>
#app {
  text-align: center;
  overflow: hidden;
  flex-direction: column;
  height: 100%;
  /* max-height: max-content; */
}
.main-container {
  height: calc(100vh - var(--ep-menu-item-height) - 3px);
}
/* .element-plus-logo {
  width: 50%;
} */
</style>
