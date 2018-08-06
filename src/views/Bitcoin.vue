
<template>
   <div>
      <h1>
          {{ price }} in {{ clicks }} clicks.
      </h1>
      <button @click="clicking()">Change Value</button>
  </div>
</template>

<script>
   export default {
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
