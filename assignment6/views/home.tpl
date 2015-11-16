    
    % include ('header.tpl', title='Hola')
    
    <div class="home">

    </div>

    <div class="login">
        <div class="login-form">

            <h1>
                Welcome to SuperNotes!
            </h1>
            <h2>
                The easiest way to save all your ideas, notes and projects in one place.
            </h2>

            <span><b>Connect to your account</b></span>
            <form action="/login" method="post">
                <div>
                    <label for="mail">
                        E-mail:
                    </label>
                    <input class="inputField" name="email" type="email" id="mail" placeholder="Your email" />
                </div>
                <div>
                    <label for="password">
                        Password:
                    </label>
                    <input class="inputField" name="password" placeholder="Password" type="password" />
                </div>
                
                <div class="button">
                    <button class="submitField" type="submit">Access account</button>
                </div>

                <p>
                    Don't you have an ccount? <a href="/register">Register!</a>
                </p>
            </form>
        </div>
    </div> 
    
    Features:
    - Save all your notes.
    - Search in all your notes.
    - Unlimited notes (premium users).

  <script src="js/scripts.js"></script>
</body>
</html>