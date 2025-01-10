import React from 'react';
import './HomePage.css';
import { useNavigate } from 'react-router-dom';
import AspectRatio from '@mui/joy/AspectRatio';
import Button from '@mui/joy/Button';
import Card from '@mui/joy/Card';
import CardContent from '@mui/joy/CardContent';


const HomePage = () => {
    const navigate = useNavigate();
    return (
        <>
            <div className='bg'>
                <div className='bgImage'></div>
                <h1 className='message'>
                    Welcome to Coach Compare
                </h1>
                {/* <Card className='searchCard' sx={{ width: 320 }}>
                    <AspectRatio minHeight="120px" maxHeight="200px">
                        <img
                        src="../images/andy_reid.jpg"
                        loading="lazy"
                        alt="Coach"
                        />
                    </AspectRatio>
                    <CardContent sx={{ display: 'flex', justifyContent: 'space-between' }}> 
                        <Button 
                            variant="solid" 
                            size="md" 
                            color="primary" 
                            aria-label="Compare" 
                            sx={{ fontWeight: 600 }}
                            onClick={() => navigate('/search')} 
                            > 
                            Explore 
                        </Button> 
                    </CardContent>
                </Card> */}
            </div>
        </>
    );
}

export default HomePage;