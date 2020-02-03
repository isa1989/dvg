<footer class="mainfooter" role="contentinfo">
  <div class="footer-middle">
    <div class="container">
      <div class="row">
        <div class="col-md-4">
          <!--Column1-->
          <div class="footer-pad">
            <h4>Digital Ventures Group</h4>
          </div>
        </div>
        <div class="col-md-3">
          <!--Column2-->
          <div class="footer-pad">
            <h4>Quick links</h4>
            <ul class="list-unstyled">
              <li><a href="index.php">Home</a></li>
              <li><a href="whatwedo.php">What we do</a></li>
              <li><a href="manifesto.php">Manifesto</a></li>
              <li><a href="joinus.php">Join us</a></li>
            </ul>
          </div>
        </div>
        <div class="col-md-5">
          <div class="footer-pad-social">
            <h4>Contact us</h4>
            <ul class="list-unstyled footer-pad-social_1">
              <li><i class="fas fa-map-marker-alt"></i> Baku, AF Business House, floor 5</li>
              <li><i class="fas fa-phone-alt"></i> +94455 XXX XX XX</li>
              <li><i class="fas fa-envelope-open"></i> info@dvg.com</li>
            </ul>
            <ul class="social-network social-circle">
              <li><a href="#" class="icoFacebook" title="Facebook"><i class="fa fa-facebook"></i></a></li>
              <li><a href="#" class="icoLinkedin" title="Linkedin"><i class="fa fa-linkedin"></i></a></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12 copy">
          <p class="text-center">&copy; Copyright 2020 - DVG.  All rights reserved.</p>
        </div>
      </div>
    </div>
  </div>
  <a href="#" class="go-top"><i class="fas fa-chevron-up"></i></a>
  <script>
    $(window).scroll(function () {
    if ($(window).scrollTop() >= 50) {
    $('#navbar_dvg').css('background','rgba(0, 0, 0 , 0.80)');
    } else {
    $('#navbar_dvg').css('background','transparent');
    }
    });
    
    
        $(document).ready(function() {
        // Show or hide the sticky footer button
        $(window).scroll(function() {
          if ($(this).scrollTop() > 200) {
            $('.go-top').fadeIn(200);
          } else {
            $('.go-top').fadeOut(200);
          }
        });
        
        // Animate the scroll to top
        $('.go-top').click(function(event) {
          event.preventDefault();
          
          $('html, body').animate({scrollTop: 0}, 300);
        })
      });
    
    
    
    AOS.init({
    duration: 1200,
    });     
    
  </script>
</footer>
</body>
</html>