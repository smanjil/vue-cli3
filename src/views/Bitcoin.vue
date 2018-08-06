
<template>
   <div>
      <h1>
          {{ price }} in {{ clicks }} clicks.
      </h1>
      <button @click="clicking()">Change Value</button>

      <hr>
      <Computed />
  </div>
</template>

<script>
    import Computed from "@/components/Computed.vue";

    export default {
        name: "computed",
        components: {
          Computed
        },
        data() {
             return {
                price: 200,
                clicks: 0
             };
          },

        methods: {
          clicking() {
             this.price = this.price + 300;
             this.clicks = this.clicks + 1;
          }
        }
    }
</script>
