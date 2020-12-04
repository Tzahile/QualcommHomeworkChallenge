<template>
  <div class="home">
    <cards-list></cards-list>
  </div>
</template>

<script>
// @ is an alias to /src
import CardsList from "@/components/cardsList.vue";

export default {
  name: "Home",
  components: {
    CardsList,
  },
};
</script>
