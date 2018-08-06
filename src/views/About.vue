<template>
  <div class="about">
    <h1>This is an about page for</h1>
    <Ether msg="Ethereum Lovers...." />
  </div>
</template>

<script>
// @ is an alias to /src
import Ether from "@/components/Ether.vue";

export default {
  name: "ether",
  components: {
    Ether
  }
};
</script>
