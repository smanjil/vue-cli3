
<template>
   <div class="container">
      <div class="panel panel-primary">
         <div class="panel-heading">
            <h3 class="panel-title">Add User</h3>
         </div>

         <div class="panel-body">
            <form>
               <div class="form-group">
                  <label for="name">Name</label>
                  <input type="text" class="form-control" placeholder="Name" v-model="name">
               </div>

               <div class="form-group">
                  <label for="email">Email</label>
                  <input type="text" class="form-control" placeholder="Email" v-model="email">
               </div>

               <div class="form-group">
                   <label class="file-label">
                        <input class="file-input" type="file" @blur="getFileName">
                        <span class="file-cta">
                            <span class="file-icon">
                                <i class="fa fa-upload"></i>
                            </span>
                            <span class="file-label">
                                Choose a file…
                            </span>
                        </span>
                        <span class="file-name">
                            {{ fname }}
                        </span>
                    </label>
               </div>

               <button type="submit" class="btn btn-primary">Submit</button>
            </form>
         </div>
      </div>

      <div class="panel panel-success"> <br>
         <div class="panel-body">
            My Name is : {{ name }} <br>
            My Email is : {{ email }} <br>
            Filename: {{ fname }} <br> <br> <br> <br>
         </div>
      </div>
   </div>
</template>

<script>
   export default {
       data () {
          return {
               name: '',
               email: '',
               fname: ''
          }
      },

      methods: {
      getFileName (e) {
            this.fpath = e.target.files[0];
            if (this.fpath){
                this.fname = this.fpath.name;
            }
        }
      }
   }
</script>
