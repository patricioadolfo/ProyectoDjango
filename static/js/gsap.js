gsap.registerPlugin(ScrollTrigger);
//document.addEventListener("DOMContentLoaded", (event) => { 
//para a recibir
gsap.to( 
    ".box4",{ 
            scrollTrigger: {
                    trigger: ".box4",
                    toggleActions: "restart none none none",
            },
            x: -30, 
            y: 5, 
            fill: '#0dcaf0', //cian
            rotation: 360, 
            duration: 4, 
            scale: 2
        });

gsap.to( 
    ".box5",{ 
        scrollTrigger: {
                trigger: ".box5",
                toggleActions: "restart none none none",
            },
        x: -15, 
        y: -20,
        fill: '#712cf9', //violeta
        rotation: 360, 
        duration: 1,
        scale: 2

        });

gsap.to( 
    ".box6",{ 
        scrollTrigger: {
                trigger: ".box6",
                toggleActions: "restart none none none",
            },
        x: 0, 
        y: 5,
        fill: '#d63384', //code
        rotation: 360, 
        duration: 2,
        scale: 2

    });

gsap.to( 
     ".box1",{
        scrollTrigger: {
                trigger: ".box1",
                toggleActions: "restart none none none",
            }, 
         x: 0,
         y: 25, 
         fill: '#d63384', //code
         rotation: 360, 
         duration: 4,
         scale: 2  
     });

gsap.to( 
    ".box2",{
        scrollTrigger: {
                trigger: ".box2",
                toggleActions: "restart none none none",
            },
        x: 0,
        y: -10, 
        fill: '#0dcaf0', //cian
        rotation: 360, 
        duration: 4, 
        scale: 2 
    });
 
gsap.to( 
    ".box3",{
        scrollTrigger: {
                trigger: ".box3",
                toggleActions: "restart none none none",
            }, 
        x: 0,
        y: 25, 
        fill: '#712cf9', //violeta
        rotation: 360, 
        duration: 4, 
        scale: 2 
    });
gsap.to( 
        ".maps1",{ 
            scrollTrigger: {
                trigger: ".maps1",
                toggleActions: "restart none none none",
            },
            x: -5,
            y: 5, 
            fill: '#712cf9',//violeta
            rotation: 360, 
            duration: 4, 
            scale: 2
        });

    gsap.to( 
        ".maps2",{
            scrollTrigger: {
                trigger: ".maps2",
                toggleActions: "restart none none none",
            }, 
            x: 0,
            y: 20, 
            fill: '#0dcaf0',//cian
            rotation: 360, 
            duration: 1, 
            scale: 2 
        });

    gsap.to( 
        ".maps3",{
            scrollTrigger: {
                trigger: ".maps3",
                toggleActions: "restart none none none",
            }, 
            x: 5,
            y: 5, 
            fill: '#d63384',//code
            rotation: 360, 
            duration: 2, 
            scale: 2 
        });
//});