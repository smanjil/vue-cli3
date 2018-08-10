

<template>
    <div class="transition">
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
        name: 'Transition',

        data () {
            return {
                items: ['first', 'second', 'third', 'fourth', 'fifth'],
                beginIndex: 0,
                acceptNum: 0,
                rejectNum: 0,
                completedMsg: '',
                sentence: ''
            }
        },

        methods: {
            submitSentence: function () {
                let formData = new FormData();
                formData.append('sentence', this.sentence);

                this.axios.post('http://127.0.0.1:5000/api/post/sentence',
                  formData,
                  {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                  }
                ).then(function(){
                  console.log('SUCCESS!!');
                })
                .catch(function(){
                  console.log('FAILURE!!');
                });
            },

            accepted: function () {
                this.beginIndex++;
                this.acceptNum++;

                this.sentence = this.items[this.beginIndex - 1];
                this.submitSentence();

                if (this.beginIndex == this.items.length){
                    $('#acceptbtn').hide();
                    $('#rejectbtn').hide();
                    this.completedMsg = 'Completed!';
                }
            },

            rejected: function () {
                this.beginIndex++;
                this.rejectNum++;

                this.sentence = this.items[this.beginIndex - 1];
                this.submitSentence(this.sentence);

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
