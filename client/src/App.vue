<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: large;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  color: #2c3e50;
}

.btn {
  text-transform: uppercase;
  min-width: 85px;
  transition-duration: 0.28s;
  transition-property: box-shadow, transform, opacity;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  line-height: 30px;
  position: relative;
  border: unset;
  box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2),
    0 2px 2px 0 rgba(87, 50, 50, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12);
  flex: 0 0 auto;
  font-weight: 600;
  letter-spacing: 0.0892857143em;
  justify-content: center;
  align-items: center;
  display: inline-block;
  cursor: pointer;
  margin: 20px;
  border-radius: 4px;
  outline: 0;
}
</style>
