<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/results/">
      
      
        <link rel="prev" href="../common-tools/">
      
      
        <link rel="next" href="../message-history/">
      
      
      <link rel="icon" href="../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>Results - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../extra/tweaks.css">
    
    <script>__md_scope=new URL("..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="Results - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/results.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/results/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="Results - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/results.png">
      
    
    
   <link href="../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#structured-result-validation" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href=".." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../img/logo-white.svg" alt="logo">

    </a>
    <label class="md-header__button md-icon" for="__drawer">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"></path></svg>
    </label>
    <div class="md-header__title" data-md-component="header-title">
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            PydanticAI
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              Results
            
          </span>
        </div>
      </div>
    </div>
    
      
        <form class="md-header__option" data-md-component="palette">
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to light mode" type="radio" name="__palette" id="__palette_0">
    
      <label class="md-header__button md-icon" title="Switch to light mode" for="__palette_1">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 2.38 1.19 4.47 3 5.74V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.26c1.81-1.27 3-3.36 3-5.74a7 7 0 0 0-7-7M9 21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1H9z"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: light)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to dark mode" type="radio" name="__palette" id="__palette_1">
    
      <label class="md-header__button md-icon" title="Switch to dark mode" for="__palette_2" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7M9 21v-1h6v1a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1m3-17a5 5 0 0 0-5 5c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58a5 5 0 0 0-5-5"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: dark)" data-md-color-scheme="slate" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to system preference" type="radio" name="__palette" id="__palette_2">
    
      <label class="md-header__button md-icon" title="Switch to system preference" for="__palette_0" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 2c3.87 0 7 3.13 7 7 0 2.38-1.19 4.47-3 5.74V17c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1v-2.26C3.19 13.47 2 11.38 2 9c0-3.87 3.13-7 7-7M6 21v-1h6v1c0 .55-.45 1-1 1H7c-.55 0-1-.45-1-1M9 4C6.24 4 4 6.24 4 9c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58 0-2.76-2.24-5-5-5m10 9h-2l-3.2 9h1.9l.7-2h3.2l.7 2h1.9zm-2.15 5.65L18 15l1.15 3.65z"></path></svg>
      </label>
    
  
</form>
      
    
    
      <script>var palette=__md_get("__palette");if(palette&&palette.color){if("(prefers-color-scheme)"===palette.color.media){var media=matchMedia("(prefers-color-scheme: light)"),input=document.querySelector(media.matches?"[data-md-color-media='(prefers-color-scheme: light)']":"[data-md-color-media='(prefers-color-scheme: dark)']");palette.color.media=input.getAttribute("data-md-color-media"),palette.color.scheme=input.getAttribute("data-md-color-scheme"),palette.color.primary=input.getAttribute("data-md-color-primary"),palette.color.accent=input.getAttribute("data-md-color-accent")}for(var[key,value]of Object.entries(palette.color))document.body.setAttribute("data-md-color-"+key,value)}</script>
    
    
    
      <label class="md-header__button md-icon" for="__search">
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"></path></svg>
      </label>
      <div class="md-search" role="dialog">
  <label class="md-search__overlay" for="__search"></label>
  <div class="md-search__inner" role="search">
    <form class="md-search__form" name="search">
      <input type="text" id="searchbox" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" required="">
      <label class="md-search__icon md-icon" for="__search">

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.516 6.516 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5Z"></path></svg>

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 11v2H8l5.5 5.5-1.42 1.42L4.16 12l7.92-7.92L13.5 5.5 8 11h12Z"></path></svg>
      </label>
      <nav class="md-search__options" aria-label="Search">

        <button id="searchbox-clear" type="reset" class="md-search__icon md-icon" title="Clear" aria-label="Clear" tabindex="-1">

          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41Z"></path></svg>
        </button>
      </nav>

        <div class="md-search__suggest"></div>

    </form>
    <div class="md-search__output">
      <div class="md-search__scrollwrap" tabindex="0">
        <div class="md-search-result">
          <div class="md-search-result__meta" id="type-to-start-searching">Type to start searching</div>
          <ol class="md-search-result__list" id="hits" role="presentation" hidden=""></ol>
        </div>
      </div>
    </div>
  </div>
</div>
    
    
      <div class="md-header__source">
        <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository">
    pydantic/pydantic-ai
  </div>
</a>
      </div>
    
  </nav>
  
</header>
    
    <div class="md-container" data-md-component="container">
      
      
        
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation">
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    



<nav class="md-nav md-nav--primary" aria-label="Navigation" data-md-level="0">
  <label class="md-nav__title" for="__drawer">
    <a href=".." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../img/logo-white.svg" alt="logo">

    </a>
    PydanticAI
  </label>
  
    <div class="md-nav__source">
      <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository">
    pydantic/pydantic-ai
  </div>
</a>
    </div>
  
  <ul class="md-nav__list">
    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href=".." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../troubleshooting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Troubleshooting
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6" checked="">
        
          
          <label class="md-nav__link" for="__nav_6" id="__nav_6_label" tabindex="">
            
  
  <span class="md-ellipsis">
    Documentation
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            Documentation
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#structured-result-validation" class="md-nav__link">
    <span class="md-ellipsis">
      Result data
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Result data">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#result-validators-functions" class="md-nav__link">
    <span class="md-ellipsis">
      Result validators functions
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#streamed-results" class="md-nav__link">
    <span class="md-ellipsis">
      Streamed Results
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Streamed Results">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#streaming-text" class="md-nav__link">
    <span class="md-ellipsis">
      Streaming Text
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#streaming-structured-responses" class="md-nav__link">
    <span class="md-ellipsis">
      Streaming Structured Responses
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#examples" class="md-nav__link">
    <span class="md-ellipsis">
      Examples
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../mcp/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    MCP
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_6_14" id="__nav_6_14_label" tabindex="0">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_14_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6_14">
            <span class="md-nav__icon md-icon"></span>
            MCP
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../cli/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Command Line Interface (CLI)
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../examples/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_7" id="__nav_7_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            Examples
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/generation/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.generation
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" style="top: 48px;">
                <div class="md-sidebar__scrollwrap" style="height: 474px;">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#structured-result-validation" class="md-nav__link">
    <span class="md-ellipsis">
      Result data
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Result data">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#result-validators-functions" class="md-nav__link">
    <span class="md-ellipsis">
      Result validators functions
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#streamed-results" class="md-nav__link">
    <span class="md-ellipsis">
      Streamed Results
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Streamed Results">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#streaming-text" class="md-nav__link">
    <span class="md-ellipsis">
      Streaming Text
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#streaming-structured-responses" class="md-nav__link">
    <span class="md-ellipsis">
      Streaming Structured Responses
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#examples" class="md-nav__link">
    <span class="md-ellipsis">
      Examples
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


  <h1>Results</h1>

<p>Results are the final values returned from <a href="../agents/#running-agents">running an agent</a>.
The result values are wrapped in <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.AgentRunResult"><code>AgentRunResult</code></a> and <a class="autorefs autorefs-internal" href="../api/result/#pydantic_ai.result.StreamedRunResult"><code>StreamedRunResult</code></a> so you can access other data like <a class="autorefs autorefs-internal" href="../api/usage/#pydantic_ai.usage.Usage">usage</a> of the run and <a href="../message-history/#accessing-messages-from-results">message history</a></p>
<p>Both <code>RunResult</code> and <code>StreamedRunResult</code> are generic in the data they wrap, so typing information about the data returned by the agent is preserved.</p>
<div class="language-python highlight"><span class="filename">olympics.py</span><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseModel</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>


<span class="k">class</span><span class="w"> </span><span class="nc">CityLocation</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">city</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">country</span><span class="p">:</span> <span class="nb">str</span>


<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'google-gla:gemini-1.5-flash'</span><span class="p">,</span> <span class="n">result_type</span><span class="o">=</span><span class="n">CityLocation</span><span class="p">)</span>
<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'Where were the olympics held in 2012?'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; city='London' country='United Kingdom'</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">usage</span><span class="p">())</span>
<span class="sd">"""</span>
<span class="sd">Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65, details=None)</span>
<span class="sd">"""</span>
</code></pre></div>
<p><em>(This example is complete, it can be run "as is")</em></p>
<p>Runs end when either a plain text response is received or the model calls a tool associated with one of the structured result types. We will add limits to make sure a run doesn't go on indefinitely, see <a href="https://github.com/pydantic/pydantic-ai/issues/70">#70</a>.</p>
<h2 id="structured-result-validation">Result data</h2>
<p>When the result type is <code>str</code>, or a union including <code>str</code>, plain text responses are enabled on the model, and the raw text response from the model is used as the response data.</p>
<p>If the result type is a union with multiple members (after remove <code>str</code> from the members), each member is registered as a separate tool with the model in order to reduce the complexity of the tool schemas and maximise the chances a model will respond correctly.</p>
<p>If the result type schema is not of type <code>"object"</code>, the result type is wrapped in a single element object, so the schema of all tools registered with the model are object schemas.</p>
<p>Structured results (like tools) use Pydantic to build the JSON schema used for the tool, and to validate the data returned by the model.</p>
<div class="admonition note">
<p class="admonition-title">Bring on PEP-747</p>
<p>Until <a href="https://peps.python.org/pep-0747/">PEP-747</a> "Annotating Type Forms" lands, unions are not valid as <code>type</code>s in Python.</p>
<p>When creating the agent we need to <code># type: ignore</code> the <code>result_type</code> argument, and add a type hint to tell type checkers about the type of the agent.</p>
</div>
<p>Here's an example of returning either text or a structured value</p>
<div class="language-python highlight"><span class="filename">box_or_error.py</span><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Union</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseModel</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>


<span class="k">class</span><span class="w"> </span><span class="nc">Box</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">width</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">height</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">units</span><span class="p">:</span> <span class="nb">str</span>


<span class="n">agent</span><span class="p">:</span> <span class="n">Agent</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="n">Box</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
    <span class="s1">'openai:gpt-4o-mini'</span><span class="p">,</span>
    <span class="n">result_type</span><span class="o">=</span><span class="n">Union</span><span class="p">[</span><span class="n">Box</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>  <span class="c1"># type: ignore</span>
    <span class="n">system_prompt</span><span class="o">=</span><span class="p">(</span>
        <span class="s2">"Extract me the dimensions of a box, "</span>
        <span class="s2">"if you can't extract all data, ask the user to try again."</span>
    <span class="p">),</span>
<span class="p">)</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'The box is 10x20x30'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; Please provide the units for the dimensions (e.g., cm, in, m).</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'The box is 10x20x30 cm'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; width=10 height=20 depth=30 units='cm'</span>
</code></pre></div>
<p><em>(This example is complete, it can be run "as is")</em></p>
<p>Here's an example of using a union return type which registered multiple tools, and wraps non-object schemas in an object:</p>
<div class="language-python highlight"><span class="filename">colors_or_sizes.py</span><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Union</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span><span class="p">:</span> <span class="n">Agent</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">list</span><span class="p">[</span><span class="nb">int</span><span class="p">]]]</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
    <span class="s1">'openai:gpt-4o-mini'</span><span class="p">,</span>
    <span class="n">result_type</span><span class="o">=</span><span class="n">Union</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">list</span><span class="p">[</span><span class="nb">int</span><span class="p">]],</span>  <span class="c1"># type: ignore</span>
    <span class="n">system_prompt</span><span class="o">=</span><span class="s1">'Extract either colors or sizes from the shapes provided.'</span><span class="p">,</span>
<span class="p">)</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'red square, blue circle, green triangle'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; ['red', 'blue', 'green']</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'square size 10, circle size 20, triangle size 30'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; [10, 20, 30]</span>
</code></pre></div>
<p><em>(This example is complete, it can be run "as is")</em></p>
<h3 id="result-validators-functions">Result validators functions</h3>
<p>Some validation is inconvenient or impossible to do in Pydantic validators, in particular when the validation requires IO and is asynchronous. PydanticAI provides a way to add validation functions via the <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.result_validator"><code>agent.result_validator</code></a> decorator.</p>
<p>Here's a simplified variant of the <a href="../examples/sql-gen/">SQL Generation example</a>:</p>
<div class="language-python highlight"><span class="filename">sql_gen.py</span><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Union</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">fake_database</span><span class="w"> </span><span class="kn">import</span> <span class="n">DatabaseConn</span><span class="p">,</span> <span class="n">QueryError</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseModel</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">RunContext</span><span class="p">,</span> <span class="n">ModelRetry</span>


<span class="k">class</span><span class="w"> </span><span class="nc">Success</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">sql_query</span><span class="p">:</span> <span class="nb">str</span>


<span class="k">class</span><span class="w"> </span><span class="nc">InvalidRequest</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">error_message</span><span class="p">:</span> <span class="nb">str</span>


<span class="n">Response</span> <span class="o">=</span> <span class="n">Union</span><span class="p">[</span><span class="n">Success</span><span class="p">,</span> <span class="n">InvalidRequest</span><span class="p">]</span>
<span class="n">agent</span><span class="p">:</span> <span class="n">Agent</span><span class="p">[</span><span class="n">DatabaseConn</span><span class="p">,</span> <span class="n">Response</span><span class="p">]</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
    <span class="s1">'google-gla:gemini-1.5-flash'</span><span class="p">,</span>
    <span class="n">result_type</span><span class="o">=</span><span class="n">Response</span><span class="p">,</span>  <span class="c1"># type: ignore</span>
    <span class="n">deps_type</span><span class="o">=</span><span class="n">DatabaseConn</span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="o">=</span><span class="s1">'Generate PostgreSQL flavored SQL queries based on user input.'</span><span class="p">,</span>
<span class="p">)</span>


<span class="nd">@agent</span><span class="o">.</span><span class="n">result_validator</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">validate_result</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">DatabaseConn</span><span class="p">],</span> <span class="n">result</span><span class="p">:</span> <span class="n">Response</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Response</span><span class="p">:</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">InvalidRequest</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">result</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">await</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="sa">f</span><span class="s1">'EXPLAIN </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">sql_query</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
    <span class="k">except</span> <span class="n">QueryError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">ModelRetry</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Invalid query: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span> <span class="kn">from</span><span class="w"> </span><span class="nn">e</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">result</span>


<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span>
    <span class="s1">'get me users who were last active yesterday.'</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">DatabaseConn</span><span class="p">()</span>
<span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; sql_query='SELECT * FROM users WHERE last_active::date = today() - interval 1 day'</span>
</code></pre></div>
<p><em>(This example is complete, it can be run "as is")</em></p>
<h2 id="streamed-results">Streamed Results</h2>
<p>There two main challenges with streamed results:</p>
<ol>
<li>Validating structured responses before they're complete, this is achieved by "partial validation" which was recently added to Pydantic in <a href="https://github.com/pydantic/pydantic/pull/10748">pydantic/pydantic#10748</a>.</li>
<li>When receiving a response, we don't know if it's the final response without starting to stream it and peeking at the content. PydanticAI streams just enough of the response to sniff out if it's a tool call or a result, then streams the whole thing and calls tools, or returns the stream as a <a class="autorefs autorefs-internal" href="../api/result/#pydantic_ai.result.StreamedRunResult"><code>StreamedRunResult</code></a>.</li>
</ol>
<h3 id="streaming-text">Streaming Text</h3>
<p>Example of streamed text result:</p>
<div class="language-python highlight"><span class="filename">streamed_hello_world.py</span><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'google-gla:gemini-1.5-flash'</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 371px; --md-tooltip-y: 57.5px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_4_annotation_1" role="tooltip"><div class="md-tooltip__inner md-typeset">Streaming works with the standard <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent"><code>Agent</code></a> class, and doesn't require any special setup, just a model that supports streaming (currently all models support streaming).</div></div><a href="#__code_4_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_stream</span><span class="p">(</span><span class="s1">'Where does "hello world" come from?'</span><span class="p">)</span> <span class="k">as</span> <span class="n">result</span><span class="p">:</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 648px; --md-tooltip-y: 133.5px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_4_annotation_2" role="tooltip"><div class="md-tooltip__inner md-typeset">The <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.run_stream"><code>Agent.run_stream()</code></a> method is used to start a streamed run, this method returns a context manager so the connection can be closed when the stream completes.</div></div><a href="#__code_4_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">result</span><span class="o">.</span><span class="n">stream_text</span><span class="p">():</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 416px; --md-tooltip-y: 152.5px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_4_annotation_3" role="tooltip"><div class="md-tooltip__inner md-typeset">Each item yield by <a class="autorefs autorefs-internal" href="../api/result/#pydantic_ai.result.StreamedRunResult.stream_text"><code>StreamedRunResult.stream_text()</code></a> is the complete text response, extended as new data is received.</div></div><a href="#__code_4_annotation_3" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="3"></span></a></aside></span>
            <span class="nb">print</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
            <span class="c1">#&gt; The first known</span>
            <span class="c1">#&gt; The first known use of "hello,</span>
            <span class="c1">#&gt; The first known use of "hello, world" was in</span>
            <span class="c1">#&gt; The first known use of "hello, world" was in a 1974 textbook</span>
            <span class="c1">#&gt; The first known use of "hello, world" was in a 1974 textbook about the C</span>
            <span class="c1">#&gt; The first known use of "hello, world" was in a 1974 textbook about the C programming language.</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is" — you'll need to add <code>asyncio.run(main())</code> to run <code>main</code>)</em></p>
<p>We can also stream text as deltas rather than the entire text in each item:</p>
<div class="language-python highlight"><span class="filename">streamed_delta_hello_world.py</span><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'google-gla:gemini-1.5-flash'</span><span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_stream</span><span class="p">(</span><span class="s1">'Where does "hello world" come from?'</span><span class="p">)</span> <span class="k">as</span> <span class="n">result</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">result</span><span class="o">.</span><span class="n">stream_text</span><span class="p">(</span><span class="n">delta</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 491px; --md-tooltip-y: 152.5px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_5_annotation_1" role="tooltip"><div class="md-tooltip__inner md-typeset"><a class="autorefs autorefs-internal" href="../api/result/#pydantic_ai.result.StreamedRunResult.stream_text"><code>stream_text</code></a> will error if the response is not text</div></div><a href="#__code_5_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
            <span class="nb">print</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
            <span class="c1">#&gt; The first known</span>
            <span class="c1">#&gt; use of "hello,</span>
            <span class="c1">#&gt; world" was in</span>
            <span class="c1">#&gt; a 1974 textbook</span>
            <span class="c1">#&gt; about the C</span>
            <span class="c1">#&gt; programming language.</span>
</code></pre></div>
<ol hidden="">
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is" — you'll need to add <code>asyncio.run(main())</code> to run <code>main</code>)</em></p>
<div class="admonition warning">
<p class="admonition-title">Result message not included in <code>messages</code></p>
<p>The final result message will <strong>NOT</strong> be added to result messages if you use <code>.stream_text(delta=True)</code>,
see <a href="../message-history/">Messages and chat history</a> for more information.</p>
</div>
<h3 id="streaming-structured-responses">Streaming Structured Responses</h3>
<p>Not all types are supported with partial validation in Pydantic, see <a href="https://github.com/pydantic/pydantic/pull/10748">pydantic/pydantic#10748</a>, generally for model-like structures it's currently best to use <code>TypeDict</code>.</p>
<p>Here's an example of streaming a use profile as it's built:</p>
<div class="language-python highlight"><span class="filename">streamed_user_profile.py</span><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">datetime</span><span class="w"> </span><span class="kn">import</span> <span class="n">date</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">typing_extensions</span><span class="w"> </span><span class="kn">import</span> <span class="n">TypedDict</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>


<span class="k">class</span><span class="w"> </span><span class="nc">UserProfile</span><span class="p">(</span><span class="n">TypedDict</span><span class="p">,</span> <span class="n">total</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">dob</span><span class="p">:</span> <span class="n">date</span>
    <span class="n">bio</span><span class="p">:</span> <span class="nb">str</span>


<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
    <span class="s1">'openai:gpt-4o'</span><span class="p">,</span>
    <span class="n">result_type</span><span class="o">=</span><span class="n">UserProfile</span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="o">=</span><span class="s1">'Extract a user profile from the input'</span><span class="p">,</span>
<span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">user_input</span> <span class="o">=</span> <span class="s1">'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_stream</span><span class="p">(</span><span class="n">user_input</span><span class="p">)</span> <span class="k">as</span> <span class="n">result</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">profile</span> <span class="ow">in</span> <span class="n">result</span><span class="o">.</span><span class="n">stream</span><span class="p">():</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">profile</span><span class="p">)</span>
            <span class="c1">#&gt; {'name': 'Ben'}</span>
            <span class="c1">#&gt; {'name': 'Ben'}</span>
            <span class="c1">#&gt; {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}</span>
            <span class="c1">#&gt; {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}</span>
            <span class="c1">#&gt; {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}</span>
            <span class="c1">#&gt; {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}</span>
            <span class="c1">#&gt; {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}</span>
</code></pre></div>
<p><em>(This example is complete, it can be run "as is" — you'll need to add <code>asyncio.run(main())</code> to run <code>main</code>)</em></p>
<p>If you want fine-grained control of validation, particularly catching validation errors, you can use the following pattern:</p>
<div class="language-python highlight"><span class="filename">streamed_user_profile.py</span><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">datetime</span><span class="w"> </span><span class="kn">import</span> <span class="n">date</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">ValidationError</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">typing_extensions</span><span class="w"> </span><span class="kn">import</span> <span class="n">TypedDict</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>


<span class="k">class</span><span class="w"> </span><span class="nc">UserProfile</span><span class="p">(</span><span class="n">TypedDict</span><span class="p">,</span> <span class="n">total</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">dob</span><span class="p">:</span> <span class="n">date</span>
    <span class="n">bio</span><span class="p">:</span> <span class="nb">str</span>


<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">,</span> <span class="n">result_type</span><span class="o">=</span><span class="n">UserProfile</span><span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">user_input</span> <span class="o">=</span> <span class="s1">'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_stream</span><span class="p">(</span><span class="n">user_input</span><span class="p">)</span> <span class="k">as</span> <span class="n">result</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">message</span><span class="p">,</span> <span class="n">last</span> <span class="ow">in</span> <span class="n">result</span><span class="o">.</span><span class="n">stream_structured</span><span class="p">(</span><span class="n">debounce_by</span><span class="o">=</span><span class="mf">0.01</span><span class="p">):</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 625px; --md-tooltip-y: 399.5px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_7_annotation_1" role="tooltip"><div class="md-tooltip__inner md-typeset"><a class="autorefs autorefs-internal" href="../api/result/#pydantic_ai.result.StreamedRunResult.stream_structured"><code>stream_structured</code></a> streams the data as <a class="autorefs autorefs-internal" href="../api/messages/#pydantic_ai.messages.ModelResponse"><code>ModelResponse</code></a> objects, thus iteration can't fail with a <code>ValidationError</code>.</div></div><a href="#__code_7_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">profile</span> <span class="o">=</span> <span class="k">await</span> <span class="n">result</span><span class="o">.</span><span class="n">validate_structured_result</span><span class="p">(</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 536px; --md-tooltip-y: 438.5px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_7_annotation_2" role="tooltip"><div class="md-tooltip__inner md-typeset"><a class="autorefs autorefs-internal" href="../api/result/#pydantic_ai.result.StreamedRunResult.validate_structured_result"><code>validate_structured_result</code></a> validates the data, <code>allow_partial=True</code> enables pydantic's <a class="autorefs autorefs-external" href="https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.validate_json"><code>experimental_allow_partial</code> flag on <code>TypeAdapter</code></a>.</div></div><a href="#__code_7_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
                    <span class="n">message</span><span class="p">,</span>
                    <span class="n">allow_partial</span><span class="o">=</span><span class="ow">not</span> <span class="n">last</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="n">ValidationError</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">profile</span><span class="p">)</span>
            <span class="c1">#&gt; {'name': 'Ben'}</span>
            <span class="c1">#&gt; {'name': 'Ben'}</span>
            <span class="c1">#&gt; {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}</span>
            <span class="c1">#&gt; {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}</span>
            <span class="c1">#&gt; {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}</span>
            <span class="c1">#&gt; {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}</span>
            <span class="c1">#&gt; {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is" — you'll need to add <code>asyncio.run(main())</code> to run <code>main</code>)</em></p>
<h2 id="examples">Examples</h2>
<p>The following examples demonstrate how to use streamed responses in PydanticAI:</p>
<ul>
<li><a href="../examples/stream-markdown/">Stream markdown</a></li>
<li><a href="../examples/stream-whales/">Stream Whales</a></li>
</ul>







  
  






                
              </article>
            </div>
          
          
  <script>var tabs=__md_get("__tabs");if(Array.isArray(tabs))e:for(var set of document.querySelectorAll(".tabbed-set")){var labels=set.querySelector(".tabbed-labels");for(var tab of tabs)for(var label of labels.getElementsByTagName("label"))if(label.innerText.trim()===tab){var input=document.getElementById(label.htmlFor);input.checked=!0;continue e}}</script>

<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
        </div>
        
      </main>
      
        <footer class="md-footer">
  
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">
  
    <div class="md-copyright__highlight">
      © Pydantic Services Inc. 2024 to present
    </div>
  
  
</div>
      
    </div>
  </div>
</footer>
      
    </div>
    <div class="md-dialog" data-md-component="dialog">
      <div class="md-dialog__inner md-typeset"></div>
    </div>
    
    
    <script id="__config" type="application/json">{"base": "..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>