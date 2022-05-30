window.onload = function() {
      var c = document.createElement("canvas");
      document.body.appendChild(c)
      var ctx = c.getContext("2d");
      c.width = window.innerWidth;
      c.height = window.innerHeight;
      let clr = 250;
      let clr1 = 10
      let then = 0;
      setTimeout(() =>{
          alert("\n\nDrag over the screen to break the lines !!!\n")
      },1500)
      var Setup = function(x, y, color) {
        this.x = rn(c.width, 0);
        this.y = rn(c.height, 0);
        this.r = 5;
        this.xv = rn(90, -90);
        this.yv = rn(90, -90);
        this.color = "hsl(" +clr+ ",100%,50%)"
      }
      Setup.prototype.update = function(td) {
        if (this.x + this.r > c.width || this.x - this.r < 0) {
          this.xv = -this.xv;

        }
        if (this.y + this.r > c.height || this.y - this.r < 0) {
          this.yv = -this.yv

        }
        let dxx = mouse.xp - this.x;
        let dyy = mouse.yp - this.y;
        let dd = Math.sqrt(dxx*dxx+dyy*dyy)
        if (dd < mouse.radius + this.r) {
          if (mouse.xp < this.x && this.x < c.width - this.r * 10) {
            this.x += 10
          }
          if (mouse.yp < this.y && this.y < c.height - this.r * 10) {
            this.y += 10
          }
          if (mouse.xp > this.x && this.x > this.r * 10) {
            this.x -= 10
          }
          if (mouse.yp > this.y && this.y > this.r * 10) {
            this.y -= 10
          }
        }
        this.x += this.xv * td;
        this.y += this.yv * td;
        this.color = "hsl(" +clr+ ",100%,50%)"
      }
      Setup.prototype.draw = function(){
        ctx.beginPath();
        ctx.fillStyle = this.color
        ctx.arc(this.x, this.y, this.r, 0, 2*Math.PI)
        ctx.fill()
      }
      const rn = (max,min) => Math.random()*(max-min)+min;
      const mouse = {
        xp: NaN,
        yp: NaN,
        radius: 90
      }
      c.addEventListener("touchstart",  e => {
        mouse.xp = e.touches[0].clientX
        mouse.yp = e.touches[0].clientY
      })
      c.addEventListener("touchmove", e => {
        mouse.xp = e.touches[0].clientX
        mouse.yp = e.touches[0].clientY
      })
      c.addEventListener("touchend", () => {
        mouse.xp = NaN
        mouse.yp = NaN
      })
      let obj = []
      const fillar = () => {
        for (let i = 0; i < 65; i++) {
        clr++
          obj.push(new Setup(clr))
        }
      }
let now = performance.now()/1000;
let dt = now - then;
then = now;
      const animate = () => {
        ctx.globalAlfa = 0.1
        ctx.fillStyle = "black"
        ctx.fillRect(0, 0, c.width, c.height)
        ctx.fill()
        clr+=2
        window.requestAnimationFrame(animate)
        for (let ii = 0; ii < obj.length; ii++) {
          obj[ii].draw()
          obj[ii].update(dt)
          for (let k = ii; k < obj.length; k++) {
            let dx = obj[k].x-obj[ii].x
            let dy = obj[k].y-obj[ii].y
            let ds = Math.sqrt(dx*dx+dy*dy)
            if (ds > (c.width/14)+(c.height/14)) {
              ctx.beginPath()
              ctx.strokeStyle = "hsla(" +clr1+ ",100%,50%,0)"
              ctx.moveTo(obj[k].x, obj[k].y)
              ctx.lineTo(obj[ii].x, obj[ii].y)
              ctx.stroke()
            } else {
              ctx.beginPath()
              ctx.strokeStyle = "hsla(" +clr+ ",100%,50%,0.8)"
              ctx.moveTo(obj[k].x, obj[k].y)
              ctx.lineTo(obj[ii].x, obj[ii].y)
              ctx.stroke()
            }
          }
        }
      }
      animate()
      fillar()
    }