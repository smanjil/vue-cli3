
<template>
    <div class="hello">
        <h1>{{ msg }}</h1>

        <transition-group name="list" tag="p">
            <span v-for="(item, index) in items" v-bind:key="item" class="list-item">
                <span v-if="index == beginIndex">
                    {{ item }}
                </span>
            </span>
        </transition-group>
        <span>{{ completedMsg }}</span>

        <button id="acceptbtn" v-on:click="accepted">Accept</button>
        <button id="rejectbtn" v-on:click="rejected">Reject</button> <br><br>

        <span>Accepted: </span> {{ acceptNum }}
        <span>Rejected: </span> {{ rejectNum }}
    </div>
</template>

<script>
    import $ from 'jquery';
    export default {
        name: 'Ethereum',

        props: {
            msg: String
        },

        data () {
            return {
                items: ['first', 'second', 'third', 'fourth', 'fifth'],
                beginIndex: 0,
                acceptNum: 0,
                rejectNum: 0,
                completedMsg: ''
            }
        },

        methods: {
            accepted: function () {
                this.beginIndex++;
                this.acceptNum++;

                if (this.beginIndex == this.items.length){
                    $('#acceptbtn').hide();
                    $('#rejectbtn').hide();
                    this.completedMsg = 'Completed!';
                }
            },

            rejected: function () {
                this.beginIndex++;
                this.rejectNum++;

                if (this.beginIndex == this.items.length){
                    $('#acceptbtn').hide();
                    $('#rejectbtn').hide();
                    this.completedMsg = 'Completed!';
                }
            }
        }
    }
</script>

<style>
    .list-item {
        display: inline-block;
    }

    .list-enter-active, .list-leave-active {
        transition: all 1s;
    }

    .list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
        opacity: 0;
        transform: translateY(30px);
    }
</style>
