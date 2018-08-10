
<template>
    <div class="prodigy">
        <ProdigyDesc msg="Welcome to Prodigy App"/>
        <Transition />
    </div>
</template>

<script>
    // @ is an alias to /src
    import ProdigyDesc from "@/components/ProdigyDesc.vue";
    import Transition from "@/components/Transition.vue";

    export default {
      name: "prodigy",
      components: {
        ProdigyDesc,
        Transition
      }
    };
</script>
